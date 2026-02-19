"""
QwenASR — WebSocket relay for Qwen3-ASR via vLLM Realtime API.
"""
import asyncio
import json
import websockets


class QwenASR:
    """Relay audio to the vLLM Qwen3-ASR Realtime API and stream back transcription deltas."""

    def __init__(
        self,
        vllm_host: str = "localhost",
        vllm_port: int = 8001,
        model: str = "Qwen/Qwen3-ASR-1.7B",
    ):
        self.ws_url = f"ws://{vllm_host}:{vllm_port}/v1/realtime"
        self.model = model

    async def handle(self, client_ws) -> None:
        """
        Main handler: connect to vLLM (Qwen), relay audio, stream transcription back.

        Same protocol as VoxtralASR.
        """
        await client_ws.send_json({"type": "status", "message": "connected"})

        try:
            async with websockets.connect(self.ws_url) as vllm_ws:
                init_msg = await vllm_ws.recv()
                print(f"[QwenASR] vLLM session: {json.loads(init_msg).get('type')}")

                await vllm_ws.send(json.dumps({
                    "type": "session.update",
                    "model": self.model,
                }))
                await vllm_ws.send(json.dumps({"type": "input_audio_buffer.commit"}))
                await client_ws.send_json({"type": "status", "message": "ready"})

                await asyncio.gather(
                    self._relay_audio(client_ws, vllm_ws),
                    self._relay_transcription(client_ws, vllm_ws),
                )

        except websockets.exceptions.ConnectionRefused:
            await client_ws.send_json({
                "type": "error",
                "message": f"Impossible de se connecter à vLLM Qwen ({self.ws_url}). Lancez le serveur d'abord.",
            })
        except Exception as e:
            await client_ws.send_json({"type": "error", "message": str(e)})

    async def _relay_audio(self, client_ws, vllm_ws) -> None:
        try:
            while True:
                raw = await client_ws.receive_text()
                msg = json.loads(raw)
                if msg.get("type") == "audio" and "data" in msg:
                    await vllm_ws.send(json.dumps({
                        "type": "input_audio_buffer.append",
                        "audio": msg["data"],
                    }))
        except Exception:
            pass

    async def _relay_transcription(self, client_ws, vllm_ws) -> None:
        try:
            async for message in vllm_ws:
                data = json.loads(message)
                if data.get("type") == "transcription.delta":
                    await client_ws.send_json({
                        "type": "transcript",
                        "text": data.get("delta", ""),
                    })
        except Exception:
            pass
