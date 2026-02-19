"""
QwenTTS — Text-to-Speech via vLLM Audio Speech API (Qwen3-TTS).
"""
import json
import httpx


class QwenTTS:
    """
    Send text to the vLLM TTS endpoint and return audio.

    Uses the OpenAI-compatible /v1/audio/speech endpoint served by vLLM-Omni.
    """

    def __init__(
        self,
        vllm_host: str = "localhost",
        vllm_port: int = 8002,
        model: str = "Qwen/Qwen3-TTS-12Hz-0.6B-Base",
        voice: str = "default",
    ):
        self.api_url = f"http://{vllm_host}:{vllm_port}/v1/audio/speech"
        self.model = model
        self.voice = voice

    async def handle(self, client_ws) -> None:
        """
        WebSocket handler for TTS.

        Protocol (client <-> this server):
          IN:  { "type": "tts", "text": "Bonjour le monde", "voice": "default" }
          OUT: { "type": "status",  "message": "connected" | "generating" }
          OUT: { "type": "audio",   "data": "<base64 wav>", "format": "wav" }
          OUT: { "type": "error",   "message": "..." }
        """
        await client_ws.send_json({"type": "status", "message": "connected"})

        try:
            while True:
                raw = await client_ws.receive_text()
                msg = json.loads(raw)

                if msg.get("type") != "tts" or not msg.get("text"):
                    continue

                text = msg["text"]
                voice = msg.get("voice", self.voice)

                await client_ws.send_json({"type": "status", "message": "generating"})

                try:
                    async with httpx.AsyncClient(timeout=30.0) as http:
                        response = await http.post(
                            self.api_url,
                            json={
                                "model": self.model,
                                "input": text,
                                "voice": voice,
                                "response_format": "wav",
                            },
                        )

                    if response.status_code == 200:
                        import base64
                        audio_b64 = base64.b64encode(response.content).decode("utf-8")
                        await client_ws.send_json({
                            "type": "audio",
                            "data": audio_b64,
                            "format": "wav",
                        })
                    else:
                        await client_ws.send_json({
                            "type": "error",
                            "message": f"vLLM TTS error ({response.status_code}): {response.text[:200]}",
                        })

                except httpx.ConnectError:
                    await client_ws.send_json({
                        "type": "error",
                        "message": f"Impossible de se connecter au serveur TTS ({self.api_url}). Lancez le serveur d'abord.",
                    })
                except Exception as e:
                    await client_ws.send_json({
                        "type": "error",
                        "message": f"TTS error: {str(e)}",
                    })

        except Exception:
            pass
