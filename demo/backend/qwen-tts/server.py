"""
Qwen3 TTS — Standalone FastAPI service.
Loads and runs Qwen3-TTS-0.6B locally via qwen-tts.
"""
import os
import io
import json
import base64
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

# ── Config ───────────────────────────────────────────────────────
MODEL = os.getenv("QWEN_TTS_MODEL", "Qwen/Qwen3-TTS-12Hz-0.6B-Base")
DEVICE = os.getenv("DEVICE", "cuda:0")
PORT = int(os.getenv("QWEN_TTS_PORT", "8084"))

app = FastAPI(title="Qwen3 TTS")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

model = None


@app.on_event("startup")
async def load_model():
    global model
    print(f"[QwenTTS] Loading {MODEL} on {DEVICE}…")
    model = Qwen3TTSModel.from_pretrained(
        MODEL,
        device_map=DEVICE,
        dtype=torch.bfloat16,
    )
    print("[QwenTTS] Model loaded.")


@app.get("/health")
async def health():
    return {"service": "qwen-tts", "model": MODEL, "loaded": model is not None}


@app.websocket("/ws/qwen-tts")
async def ws_qwen_tts(ws: WebSocket):
    await ws.accept()
    await ws.send_json({"type": "status", "message": "connected"})

    if model is None:
        await ws.send_json({"type": "error", "message": "Model not loaded."})
        return

    try:
        while True:
            raw = await ws.receive_text()
            msg = json.loads(raw)

            if msg.get("type") != "tts" or not msg.get("text"):
                continue

            text = msg["text"]
            language = msg.get("language", "French")
            prompt_audio_b64 = msg.get("prompt_audio")
            prompt_text = msg.get("prompt_text")

            await ws.send_json({"type": "status", "message": "generating"})

            try:
                ref_audio_path = None
                if prompt_audio_b64:
                    import tempfile
                    # Save base64 prompt to a temp wav file
                    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                        f.write(base64.b64decode(prompt_audio_b64))
                        ref_audio_path = f.name

                # Calling model with expected params: text, language, ref_audio, prompt_text
                wavs, sr = model.generate_voice_clone(
                    text=text,
                    language=language,
                    ref_audio=ref_audio_path,
                    prompt_text=prompt_text
                )

                if ref_audio_path and os.path.exists(ref_audio_path):
                    os.remove(ref_audio_path)

                buf = io.BytesIO()
                sf.write(buf, wavs[0], sr, format="WAV")
                buf.seek(0)
                audio_b64 = base64.b64encode(buf.read()).decode("utf-8")

                await ws.send_json({"type": "audio", "data": audio_b64, "format": "wav"})

            except Exception as e:
                await ws.send_json({"type": "error", "message": f"TTS error: {str(e)}"})

    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True)
