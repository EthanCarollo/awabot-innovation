"""
Voxtral Demo — Multi-Service Backend
=====================================
FastAPI server with 3 WebSocket endpoints:
  - /ws/voxtral   → Voxtral ASR (transcription)
  - /ws/qwen-asr  → Qwen3 ASR (transcription)
  - /ws/qwen-tts  → Qwen3 TTS (text-to-speech)

Usage:
    uvicorn server:app --host 0.0.0.0 --port 8080 --reload
"""

import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from voxtral_asr import VoxtralASR
from qwen_asr import QwenASR
from qwen_tts import QwenTTS

# ── Config ───────────────────────────────────────────────────────
VLLM_HOST = os.getenv("VLLM_HOST", "localhost")

app = FastAPI(title="Awabot Demo Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Service instances ────────────────────────────────────────────
voxtral = VoxtralASR(
    vllm_host=VLLM_HOST,
    vllm_port=int(os.getenv("VOXTRAL_PORT", "8000")),
    model=os.getenv("VOXTRAL_MODEL", "mistralai/Voxtral-Mini-4B-Realtime-2602"),
)

qwen_asr = QwenASR(
    vllm_host=VLLM_HOST,
    vllm_port=int(os.getenv("QWEN_ASR_PORT", "8001")),
    model=os.getenv("QWEN_ASR_MODEL", "Qwen/Qwen3-ASR-1.7B"),
)

qwen_tts = QwenTTS(
    vllm_host=VLLM_HOST,
    vllm_port=int(os.getenv("QWEN_TTS_PORT", "8002")),
    model=os.getenv("QWEN_TTS_MODEL", "Qwen/Qwen3-TTS-12Hz-0.6B-Base"),
)


# ── Health ───────────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "services": {
            "voxtral_asr": {"url": voxtral.ws_url, "model": voxtral.model},
            "qwen_asr": {"url": qwen_asr.ws_url, "model": qwen_asr.model},
            "qwen_tts": {"url": qwen_tts.api_url, "model": qwen_tts.model},
        },
    }


# ── WebSocket endpoints ─────────────────────────────────────────
@app.websocket("/ws/voxtral")
async def ws_voxtral(ws: WebSocket):
    await ws.accept()
    try:
        await voxtral.handle(ws)
    except WebSocketDisconnect:
        pass
    finally:
        try:
            await ws.close()
        except Exception:
            pass


@app.websocket("/ws/qwen-asr")
async def ws_qwen_asr(ws: WebSocket):
    await ws.accept()
    try:
        await qwen_asr.handle(ws)
    except WebSocketDisconnect:
        pass
    finally:
        try:
            await ws.close()
        except Exception:
            pass


@app.websocket("/ws/qwen-tts")
async def ws_qwen_tts(ws: WebSocket):
    await ws.accept()
    try:
        await qwen_tts.handle(ws)
    except WebSocketDisconnect:
        pass
    finally:
        try:
            await ws.close()
        except Exception:
            pass
