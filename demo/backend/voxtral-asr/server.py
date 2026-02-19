import os
import json
import base64
import asyncio
from dotenv import load_dotenv
from mistralai import Mistral
from mistralai.models import AudioFormat, RealtimeTranscriptionError, RealtimeTranscriptionSessionCreated, TranscriptionStreamDone, TranscriptionStreamTextDelta
from mistralai.extra.realtime import UnknownRealtimeEvent

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

# ── Load Environment ─────────────────────────────────────────────
load_dotenv()

# ── Config ───────────────────────────────────────────────────────
API_KEY = os.getenv("MISTRAL_API_KEY")
MODEL = os.getenv("VOXTRAL_MODEL", "voxtral-mini-transcribe-realtime-2602")
PORT = int(os.getenv("VOXTRAL_PORT", "8082"))

app = FastAPI(title="Voxtral ASR (API)")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

if not API_KEY:
    print("[VoxtralASR] WARNING: MISTRAL_API_KEY not found in .env")

# Microphone is always pcm_s16le at 16000Hz in our frontend
AUDIO_FORMAT = AudioFormat(encoding="pcm_s16le", sample_rate=16000)

@app.get("/health")
async def health():
    return {"service": "voxtral-asr", "mode": "api", "model": MODEL}


@app.websocket("/ws/voxtral")
async def ws_voxtral(ws: WebSocket):
    await ws.accept()
    await ws.send_json({"type": "status", "message": "connected"})

    if not API_KEY:
        await ws.send_json({"type": "error", "message": "API Key missing."})
        return

    client = Mistral(api_key=API_KEY)
    audio_queue = asyncio.Queue()

    async def mistral_streamer():
        try:
            full_transcript = ""

            async def audio_iterator():
                while True:
                    chunk = await audio_queue.get()
                    if chunk is None: break
                    yield chunk

            async for event in client.audio.realtime.transcribe_stream(
                audio_stream=audio_iterator(),
                model=MODEL,
                audio_format=AUDIO_FORMAT
            ):
                if isinstance(event, RealtimeTranscriptionSessionCreated):
                    print(f"[VoxtralASR] Session created: {event}")
                    await ws.send_json({"type": "status", "message": "session_created"})
                
                elif isinstance(event, TranscriptionStreamTextDelta):
                    full_transcript += event.text
                    await ws.send_json({
                        "type": "transcript", 
                        "text": full_transcript,
                        "is_final": False
                    })
                
                elif isinstance(event, TranscriptionStreamDone):
                    # Mistral Done event contains the final combined text
                    await ws.send_json({
                        "type": "transcript", 
                        "text": event.text,
                        "is_final": True
                    })
                    full_transcript = "" # Reset for next potential use in same connection (though we usually have 1 session)
                
                elif isinstance(event, RealtimeTranscriptionError):
                    print(f"[VoxtralASR] API Error: {event.message}")
                    await ws.send_json({"type": "error", "message": event.message})
                
                elif isinstance(event, UnknownRealtimeEvent):
                    continue

        except Exception as e:
            print(f"[VoxtralASR] Mistral Stream Error: {e}")
            await ws.send_json({"type": "error", "message": str(e)})

    stream_task = asyncio.create_task(mistral_streamer())
    await ws.send_json({"type": "status", "message": "ready"})

    try:
        while True:
            raw = await ws.receive_text()
            msg = json.loads(raw)

            if msg.get("type") == "audio" and "data" in msg:
                chunk_bytes = base64.b64decode(msg["data"])
                await audio_queue.put(chunk_bytes)

    except WebSocketDisconnect:
        pass
    finally:
        await audio_queue.put(None)
        stream_task.cancel()
        try:
            await stream_task
        except asyncio.CancelledError:
            pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True, reload_excludes=["*.log", "*.txt"])


