"""
Qwen3 ASR — Standalone FastAPI service.
Loads and runs Qwen3-ASR-1.7B locally via qwen-asr.
"""
import os
import json
import base64
import numpy as np
import torch
from qwen_asr import Qwen3ASRModel

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

# ── Config ───────────────────────────────────────────────────────
MODEL = os.getenv("QWEN_ASR_MODEL", "Qwen/Qwen3-ASR-1.7B")
DEVICE = os.getenv("DEVICE", "cuda:0")
PORT = int(os.getenv("QWEN_ASR_PORT", "8083"))

app = FastAPI(title="Qwen3 ASR")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

model = None


@app.on_event("startup")
async def load_model():
    global model
    print(f"[QwenASR] Loading {MODEL} on {DEVICE}…")
    model = Qwen3ASRModel.from_pretrained(
        MODEL,
        dtype=torch.bfloat16,
        device_map=DEVICE,
        max_new_tokens=256,
    )
    print("[QwenASR] Model loaded.")
    
    print("[QwenASR] Model loaded.")


@app.get("/health")
async def health():
    return {"service": "qwen-asr", "model": MODEL, "loaded": model is not None}


@app.websocket("/ws/qwen-asr")
async def ws_qwen_asr(ws: WebSocket):
    await ws.accept()
    await ws.send_json({"type": "status", "message": "connected"})

    if model is None:
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

                # Process if we have enough audio (e.g., every 0.25s roughly)
                if len(audio_buffer) >= 8000: 
                    pcm = np.frombuffer(bytes(audio_buffer), dtype=np.int16)
                    # Limit window to last 7 seconds to keep latency low
                    WINDOW_SIZE = 16000 * 7
                    if len(pcm) > WINDOW_SIZE:
                        pcm = pcm[-WINDOW_SIZE:]
                    
                    audio_float = pcm.astype(np.float32) / 32768.0

                    results = model.transcribe(
                        audio=[(audio_float, 16000)],
                        language=None,
                    )

                    if results and results[0].text:
                        text = results[0].text.strip()
                        await ws.send_json({
                            "type": "transcript", 
                            "text": text,
                            "is_final": current_silence_duration >= SILENCE_DURATION_LIMIT
                        })

                    # If silence is long enough, we clear buffer
                    if current_silence_duration >= SILENCE_DURATION_LIMIT:
                        audio_buffer.clear()
                        current_silence_duration = 0.0
                    elif len(audio_buffer) > MAX_BUFFER_SIZE:
                        # Fallback for very long speech without silence: 
                        # just keep the last few samples to maintain context
                        new_buffer = audio_buffer[-8000:]
                        audio_buffer.clear()
                        audio_buffer.extend(new_buffer)

    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True, reload_excludes=["*.log", "*.txt"])
