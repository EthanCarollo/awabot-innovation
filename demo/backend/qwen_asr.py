"""
QwenASR — Local inference via qwen-asr package.
"""
import io
import json
import base64
import numpy as np
import torch
from qwen_asr import Qwen3ASRModel


class QwenASR:
    """Load Qwen3-ASR locally and transcribe audio chunks."""

    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-ASR-1.7B",
        device: str = "cuda:0",
    ):
        self.model_name = model_name
        self.device = device
        self.model = None

    def load(self) -> None:
        """Load the model into GPU memory. Called once at startup."""
        print(f"[QwenASR] Loading {self.model_name} on {self.device}…")
        self.model = Qwen3ASRModel.from_pretrained(
            self.model_name,
            dtype=torch.bfloat16,
            device_map=self.device,
            max_new_tokens=256,
        )
        print(f"[QwenASR] Model loaded.")

    async def handle(self, client_ws) -> None:
        """
        WebSocket handler.

        Protocol:
          IN:  { "type": "audio", "data": "<base64 PCM16 16kHz>" }
          OUT: { "type": "transcript", "text": "<full transcription>" }
          OUT: { "type": "status",  "message": "connected" | "ready" }
          OUT: { "type": "error",   "message": "..." }
        """
        await client_ws.send_json({"type": "status", "message": "connected"})

        if self.model is None:
            await client_ws.send_json({"type": "error", "message": "Model not loaded."})
            return

        await client_ws.send_json({"type": "status", "message": "ready"})

        # Accumulate audio chunks, transcribe on demand
        audio_buffer = bytearray()

        try:
            while True:
                raw = await client_ws.receive_text()
                msg = json.loads(raw)

                if msg.get("type") == "audio" and "data" in msg:
                    # Decode base64 PCM16 and accumulate
                    pcm_bytes = base64.b64decode(msg["data"])
                    audio_buffer.extend(pcm_bytes)

                    # Transcribe every ~1 second of audio (16000 samples * 2 bytes)
                    if len(audio_buffer) >= 32000:
                        pcm = np.frombuffer(bytes(audio_buffer), dtype=np.int16)
                        audio_float = pcm.astype(np.float32) / 32767.0

                        results = self.model.transcribe(
                            audio=[(audio_float, 16000)],
                            language=None,
                        )

                        if results and results[0].text:
                            await client_ws.send_json({
                                "type": "transcript",
                                "text": results[0].text + " ",
                            })

                        audio_buffer.clear()

        except Exception:
            pass
