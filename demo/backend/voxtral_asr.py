"""
VoxtralASR — WebSocket relay for Voxtral Realtime API.
"""
import asyncio
import json
import websockets


class VoxtralASR:
    """Relay audio to the vLLM Voxtral Realtime API and stream back transcription deltas."""

    def __init__(
        self,
        vllm_host: str = "localhost",
        vllm_port: int = 8000,
        model: str = "mistralai/Voxtral-Mini-4B-Realtime-2602",
    ):
        self.ws_url = f"ws://{vllm_host}:{vllm_port}/v1/realtime"
        self.model = model

    async def handle(self, client_ws) -> None:
        """
        Main handler: connect to vLLM, relay audio from client, stream transcription back.

        Protocol (client <-> this server):
          IN:  { "type": "audio", "data": "<base64 PCM16 16kHz>" }
          OUT: { "type": "transcript", "text": "<delta>" }
          OUT: { "type": "status",  "message": "connected" | "ready" }
          OUT: { "type": "error",   "message": "..." }
        """
        await client_ws.send_json({"type": "status", "message": "connected"})

        try:
            async with websockets.connect(self.ws_url) as vllm_ws:
                # Wait for session.created
                init_msg = await vllm_ws.recv()
                print(f"[VoxtralASR] vLLM session: {json.loads(init_msg).get('type')}")

                # Configure
                await vllm_ws.send(json.dumps({
                    "type": "session.update",
                    "model": self.model,
                }))
                await vllm_ws.send(json.dumps({"type": "input_audio_buffer.commit"}))
                await client_ws.send_json({"type": "status", "message": "ready"})

                # Two concurrent relays
                await asyncio.gather(
                    self._relay_audio(client_ws, vllm_ws),
                    self._relay_transcription(client_ws, vllm_ws),
                )

        except websockets.exceptions.ConnectionRefused:
            await client_ws.send_json({
                "type": "error",
                "message": f"Impossible de se connecter à vLLM ({self.ws_url}). Lancez le serveur d'abord.",
            })
        except Exception as e:
            await client_ws.send_json({"type": "error", "message": str(e)})

    async def _relay_audio(self, client_ws, vllm_ws) -> None:
        """Forward audio chunks from the client to vLLM."""
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
        """Forward transcription deltas from vLLM to the client."""
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
