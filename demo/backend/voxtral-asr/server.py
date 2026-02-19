"""
Voxtral ASR — Standalone FastAPI service.
Loads and runs Voxtral Mini 4B via vLLM locally.
"""
import os
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
    llm = LLM(model=MODEL, dtype="bfloat16", max_model_len=4096)
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

    try:
        while True:
            raw = await ws.receive_text()
            msg = json.loads(raw)

            if msg.get("type") == "audio" and "data" in msg:
                audio_buffer.extend(base64.b64decode(msg["data"]))

                if len(audio_buffer) >= 32000:
                    pcm = np.frombuffer(bytes(audio_buffer), dtype=np.int16)
                    audio_float = pcm.astype(np.float32) / 32767.0

                    loop = asyncio.get_event_loop()
                    result = await loop.run_in_executor(None, _transcribe, audio_float)

                    if result:
                        await ws.send_json({"type": "transcript", "text": result + " "})
                    audio_buffer.clear()

    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True)
