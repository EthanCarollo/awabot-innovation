import os
os.environ["VLLM_USE_V1"] = "0" # Retired in 0.15.1? Let's check if it still works as fallback.
# os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
os.environ["VLLM_LOGGING_LEVEL"] = "DEBUG"

import json
import base64
import asyncio
import numpy as np

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

try:
    from vllm import LLM, SamplingParams
    VLLM_AVAILABLE = True
except ImportError:
    VLLM_AVAILABLE = False

# ── Config ───────────────────────────────────────────────────────
MODEL = os.getenv("VOXTRAL_MODEL", "mistralai/Voxtral-Mini-4B-Realtime-2602")
DEVICE = os.getenv("DEVICE", "cuda:0")
PORT = int(os.getenv("VOXTRAL_PORT", "8082"))

app = FastAPI(title="Voxtral ASR")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

llm = None


@app.on_event("startup")
async def load_model():
    global llm
    if not VLLM_AVAILABLE:
        print("[VoxtralASR] vLLM not installed. Endpoint will return errors.")
        return
    print(f"[VoxtralASR] Loading {MODEL} via vLLM…")
    llm = LLM(
        model=MODEL, 
        dtype="bfloat16", 
        trust_remote_code=True,
        max_model_len=4096,
        hf_overrides={"sliding_window": 4096},
        enforce_eager=True,
        gpu_memory_utilization=0.7
    )
    print("[VoxtralASR] Model loaded.")


@app.get("/health")
async def health():
    return {"service": "voxtral-asr", "model": MODEL, "loaded": llm is not None}


def _transcribe(audio_float: np.ndarray) -> str:
    try:
        params = SamplingParams(temperature=0.0, max_tokens=256)
        outputs = llm.generate(
            [{"prompt": "<|audio|>", "multi_modal_data": {"audio": (audio_float, 16000)}}],
            sampling_params=params,
        )
        if outputs and outputs[0].outputs:
            return outputs[0].outputs[0].text.strip()
    except Exception as e:
        print(f"[VoxtralASR] Error: {e}")
    return ""


@app.websocket("/ws/voxtral")
async def ws_voxtral(ws: WebSocket):
    await ws.accept()
    await ws.send_json({"type": "status", "message": "connected"})

    if llm is None:
        await ws.send_json({"type": "error", "message": "Model not loaded."})
        return

    await ws.send_json({"type": "status", "message": "ready"})
    audio_buffer = bytearray()
    
    # VAD & Incremental Buffering state
    MAX_BUFFER_SIZE = 16000 * 2 * 30  # 30 seconds max
    SILENCE_THRESHOLD = 0.01  # RMS threshold
    SILENCE_DURATION_LIMIT = 0.8  # seconds
    
    current_silence_duration = 0.0

    try:
        while True:
            raw = await ws.receive_text()
            msg = json.loads(raw)

            if msg.get("type") == "audio" and "data" in msg:
                chunk_bytes = base64.b64decode(msg["data"])
                audio_buffer.extend(chunk_bytes)
                
                # Check for silence in the new chunk
                chunk_pcm = np.frombuffer(chunk_bytes, dtype=np.int16)
                chunk_float = chunk_pcm.astype(np.float32) / 32768.0
                rms = np.sqrt(np.mean(chunk_float**2)) if len(chunk_float) > 0 else 0
                
                chunk_duration = len(chunk_pcm) / 16000.0
                if rms < SILENCE_THRESHOLD:
                    current_silence_duration += chunk_duration
                else:
                    current_silence_duration = 0.0

                # Process every ~0.25s of audio to keep latency low
                if len(audio_buffer) >= 8000:
                    pcm = np.frombuffer(bytes(audio_buffer), dtype=np.int16)
                    # Limit window to last 7 seconds to keep latency low
                    WINDOW_SIZE = 16000 * 7
                    if len(pcm) > WINDOW_SIZE:
                        pcm = pcm[-WINDOW_SIZE:]
                        
                    audio_float = pcm.astype(np.float32) / 32768.0

                    loop = asyncio.get_event_loop()
                    result = await loop.run_in_executor(None, _transcribe, audio_float)

                    if result:
                        await ws.send_json({
                            "type": "transcript", 
                            "text": result,
                            "is_final": current_silence_duration >= SILENCE_DURATION_LIMIT
                        })

                    # If silence is long enough, we clear buffer
                    if current_silence_duration >= SILENCE_DURATION_LIMIT:
                        audio_buffer.clear()
                        current_silence_duration = 0.0
                    elif len(audio_buffer) > MAX_BUFFER_SIZE:
                        # Fallback: keep just the end for context
                        new_buffer = audio_buffer[-8000:]
                        audio_buffer.clear()
                        audio_buffer.extend(new_buffer)

    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True)
