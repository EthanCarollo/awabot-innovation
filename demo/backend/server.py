"""
Voxtral Demo — Backend WebSocket Relay
=======================================
FastAPI server that relays audio from the Nuxt frontend to the vLLM
Realtime API and streams transcription deltas back.

Usage:
    uvicorn server:app --host 0.0.0.0 --port 8080 --reload
"""

import asyncio
import json
import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import websockets

# ── Config ───────────────────────────────────────────────────────
VLLM_HOST = os.getenv("VLLM_HOST", "localhost")
VLLM_PORT = os.getenv("VLLM_PORT", "8000")
VLLM_MODEL = os.getenv("VLLM_MODEL", "mistralai/Voxtral-Mini-4B-Realtime-2602")
VLLM_WS_URL = f"ws://{VLLM_HOST}:{VLLM_PORT}/v1/realtime"

app = FastAPI(title="Voxtral Demo Backend")

# CORS — allow the Nuxt dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok", "vllm_url": VLLM_WS_URL, "model": VLLM_MODEL}


@app.websocket("/ws/transcribe")
async def transcribe(ws: WebSocket):
    """
    WebSocket endpoint for the frontend.

    Protocol:
      Frontend -> Backend:  { "type": "audio", "data": "<base64 PCM16 16kHz>" }
      Backend -> Frontend:  { "type": "transcript", "text": "<delta text>" }
      Backend -> Frontend:  { "type": "error", "message": "..." }
      Backend -> Frontend:  { "type": "status", "message": "connected" | "ready" }
    """
    await ws.accept()
    await ws.send_json({"type": "status", "message": "connected"})

    try:
        async with websockets.connect(VLLM_WS_URL) as vllm_ws:
            # Wait for session.created from vLLM
            init_msg = await vllm_ws.recv()
            print(f"✅ vLLM session: {json.loads(init_msg).get('type', 'unknown')}")

            # Configure model
            await vllm_ws.send(json.dumps({
                "type": "session.update",
                "model": VLLM_MODEL,
            }))

            # Signal ready
            await vllm_ws.send(json.dumps({"type": "input_audio_buffer.commit"}))
            await ws.send_json({"type": "status", "message": "ready"})

            # ── Two concurrent tasks ──
            async def relay_audio():
                """Frontend → vLLM: forward audio chunks."""
                try:
                    while True:
                        raw = await ws.receive_text()
                        msg = json.loads(raw)
                        if msg.get("type") == "audio" and "data" in msg:
                            await vllm_ws.send(json.dumps({
                                "type": "input_audio_buffer.append",
                                "audio": msg["data"],
                            }))
                except WebSocketDisconnect:
                    pass

            async def relay_transcription():
                """vLLM → Frontend: forward transcription deltas."""
                try:
                    async for message in vllm_ws:
                        data = json.loads(message)
                        if data.get("type") == "transcription.delta":
                            await ws.send_json({
                                "type": "transcript",
                                "text": data.get("delta", ""),
                            })
                except Exception:
                    pass

            await asyncio.gather(relay_audio(), relay_transcription())

    except websockets.exceptions.ConnectionRefused:
        await ws.send_json({
            "type": "error",
            "message": f"Impossible de se connecter au serveur vLLM ({VLLM_WS_URL}). Lancez d'abord: bash serve.sh",
        })
    except Exception as e:
        await ws.send_json({
            "type": "error",
            "message": f"Erreur: {str(e)}",
        })
    finally:
        try:
            await ws.close()
        except Exception:
            pass
