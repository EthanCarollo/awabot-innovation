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

    try:
        while True:
            raw = await ws.receive_text()
            msg = json.loads(raw)

            if msg.get("type") == "audio" and "data" in msg:
                audio_buffer.extend(base64.b64decode(msg["data"]))

                if len(audio_buffer) >= 32000:
                    pcm = np.frombuffer(bytes(audio_buffer), dtype=np.int16)
                    audio_float = pcm.astype(np.float32) / 32767.0

                    results = model.transcribe(
                        audio=[(audio_float, 16000)],
                        language=None,
                    )

                    if results and results[0].text:
                        await ws.send_json({"type": "transcript", "text": results[0].text + " "})

                    audio_buffer.clear()

    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True)
