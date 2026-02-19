"""
VoxtralASR — Local inference via vLLM Python API.

Voxtral requires vLLM for efficient GPU inference (no standalone transformers support).
We use the vLLM offline inference API to run the model locally.
"""
import json
import base64
import asyncio
import numpy as np
import torch

try:
    from vllm import LLM, SamplingParams
    VLLM_AVAILABLE = True
except ImportError:
    VLLM_AVAILABLE = False


class VoxtralASR:
    """Load Voxtral via vLLM offline API and transcribe audio chunks."""

    def __init__(
        self,
        model_name: str = "mistralai/Voxtral-Mini-4B-Realtime-2602",
        device: str = "cuda:0",
    ):
        self.model_name = model_name
        self.device = device
        self.llm = None

    def load(self) -> None:
        """Load the Voxtral model via vLLM. Called once at startup."""
        if not VLLM_AVAILABLE:
            print("[VoxtralASR] vLLM not installed — Voxtral will not be available.")
            return

        print(f"[VoxtralASR] Loading {self.model_name} via vLLM…")
        self.llm = LLM(
            model=self.model_name,
            dtype="bfloat16",
            max_model_len=4096,
        )
        print(f"[VoxtralASR] Model loaded.")

    async def handle(self, client_ws) -> None:
        """
        WebSocket handler.

        Protocol: same as QwenASR.
        """
        await client_ws.send_json({"type": "status", "message": "connected"})

        if self.llm is None:
            msg = "vLLM not installed or model not loaded." if not VLLM_AVAILABLE else "Model not loaded."
            await client_ws.send_json({"type": "error", "message": msg})
            return

        await client_ws.send_json({"type": "status", "message": "ready"})

        audio_buffer = bytearray()

        try:
            while True:
                raw = await client_ws.receive_text()
                msg = json.loads(raw)

                if msg.get("type") == "audio" and "data" in msg:
                    pcm_bytes = base64.b64decode(msg["data"])
                    audio_buffer.extend(pcm_bytes)

                    # Transcribe every ~1 second of audio
                    if len(audio_buffer) >= 32000:
                        pcm = np.frombuffer(bytes(audio_buffer), dtype=np.int16)
                        audio_float = pcm.astype(np.float32) / 32767.0

                        # Run vLLM inference in a thread to not block the event loop
                        loop = asyncio.get_event_loop()
                        result = await loop.run_in_executor(
                            None,
                            self._transcribe,
                            audio_float,
                        )

                        if result:
                            await client_ws.send_json({
                                "type": "transcript",
                                "text": result + " ",
                            })

                        audio_buffer.clear()

        except Exception:
            pass

    def _transcribe(self, audio_float: np.ndarray) -> str:
        """Run vLLM offline inference for Voxtral."""
        try:
            sampling_params = SamplingParams(
                temperature=0.0,
                max_tokens=256,
            )

            # Voxtral expects audio as a multi-modal input
            outputs = self.llm.generate(
                [{
                    "prompt": "<|audio|>",
                    "multi_modal_data": {
                        "audio": (audio_float, 16000),
                    },
                }],
                sampling_params=sampling_params,
            )

            if outputs and outputs[0].outputs:
                return outputs[0].outputs[0].text.strip()
        except Exception as e:
            print(f"[VoxtralASR] Transcription error: {e}")

        return ""
