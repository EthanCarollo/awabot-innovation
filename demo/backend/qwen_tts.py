"""
QwenTTS — Local inference via qwen-tts package.
"""
import io
import json
import base64
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel


class QwenTTS:
    """Load Qwen3-TTS locally and generate speech from text."""

    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-TTS-12Hz-0.6B-Base",
        device: str = "cuda:0",
    ):
        self.model_name = model_name
        self.device = device
        self.model = None

    def load(self) -> None:
        """Load the model into GPU memory. Called once at startup."""
        print(f"[QwenTTS] Loading {self.model_name} on {self.device}…")
        self.model = Qwen3TTSModel.from_pretrained(
            self.model_name,
            device_map=self.device,
            dtype=torch.bfloat16,
        )
        print(f"[QwenTTS] Model loaded.")

    async def handle(self, client_ws) -> None:
        """
        WebSocket handler.

        Protocol:
          IN:  { "type": "tts", "text": "Bonjour", "language": "French" }
          OUT: { "type": "status",  "message": "connected" | "generating" }
          OUT: { "type": "audio",   "data": "<base64 wav>", "format": "wav" }
          OUT: { "type": "error",   "message": "..." }
        """
        await client_ws.send_json({"type": "status", "message": "connected"})

        if self.model is None:
            await client_ws.send_json({"type": "error", "message": "Model not loaded."})
            return

        try:
            while True:
                raw = await client_ws.receive_text()
                msg = json.loads(raw)

                if msg.get("type") != "tts" or not msg.get("text"):
                    continue

                text = msg["text"]
                language = msg.get("language", "French")

                await client_ws.send_json({"type": "status", "message": "generating"})

                try:
                    # Generate speech
                    wavs, sr = self.model.generate_voice_clone(
                        text=text,
                        language=language,
                    )

                    # Encode to WAV bytes
                    buf = io.BytesIO()
                    sf.write(buf, wavs[0], sr, format="WAV")
                    buf.seek(0)
                    audio_b64 = base64.b64encode(buf.read()).decode("utf-8")

                    await client_ws.send_json({
                        "type": "audio",
                        "data": audio_b64,
                        "format": "wav",
                    })

                except Exception as e:
                    await client_ws.send_json({
                        "type": "error",
                        "message": f"TTS generation error: {str(e)}",
                    })

        except Exception:
            pass
