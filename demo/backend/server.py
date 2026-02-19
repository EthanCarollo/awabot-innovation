"""
Awabot Demo — Multi-Service Backend
====================================
FastAPI server that loads and runs AI models locally.

Endpoints:
  - /ws/voxtral   -> Voxtral ASR (via vLLM)
  - /ws/qwen-asr  -> Qwen3 ASR (via qwen-asr)
  - /ws/qwen-tts  -> Qwen3 TTS (via qwen-tts)

Usage:
    uvicorn server:app --host 0.0.0.0 --port 8082 --reload
"""

import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from voxtral_asr import VoxtralASR
from qwen_asr import QwenASR
from qwen_tts import QwenTTS

# ── Config ───────────────────────────────────────────────────────
DEVICE = os.getenv("DEVICE", "cuda:0")

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
    model_name=os.getenv("VOXTRAL_MODEL", "mistralai/Voxtral-Mini-4B-Realtime-2602"),
    device=DEVICE,
)

qwen_asr = QwenASR(
    model_name=os.getenv("QWEN_ASR_MODEL", "Qwen/Qwen3-ASR-1.7B"),
    device=DEVICE,
)

qwen_tts = QwenTTS(
    model_name=os.getenv("QWEN_TTS_MODEL", "Qwen/Qwen3-TTS-12Hz-0.6B-Base"),
    device=DEVICE,
)


# ── Startup: load models ────────────────────────────────────────
@app.on_event("startup")
async def load_models():
    """Load all models into GPU at startup."""
    # Load each model — failures are non-fatal (endpoint will report error)
    for name, service in [("Voxtral", voxtral), ("QwenASR", qwen_asr), ("QwenTTS", qwen_tts)]:
        try:
            service.load()
        except Exception as e:
            print(f"[Startup] Failed to load {name}: {e}")


# ── Health ───────────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "services": {
            "voxtral_asr": {"model": voxtral.model_name, "loaded": voxtral.llm is not None},
            "qwen_asr": {"model": qwen_asr.model_name, "loaded": qwen_asr.model is not None},
            "qwen_tts": {"model": qwen_tts.model_name, "loaded": qwen_tts.model is not None},
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
