# Backend — Awabot Demo

Serveur FastAPI exposant 3 endpoints WebSocket pour les services d'IA.

## Prérequis

> **Important** : Ce backend est concu et optimise pour une inference GPU **NVIDIA (CUDA)**.
> Les modeles vLLM utilises ne sont pas compatibles avec Apple MLX, AMD ROCm ou inference CPU.
> Un GPU avec minimum **16 Go de VRAM** est recommande (ex: RTX 4090, A100, L40).

## Endpoints

| Endpoint | Service | Modele | Port vLLM |
|---|---|---|---|
| `/ws/voxtral` | Voxtral ASR | `mistralai/Voxtral-Mini-4B-Realtime-2602` | 8000 |
| `/ws/qwen-asr` | Qwen3 ASR | `Qwen/Qwen3-ASR-1.7B` | 8001 |
| `/ws/qwen-tts` | Qwen3 TTS | `Qwen/Qwen3-TTS-12Hz-0.6B-Base` | 8002 |

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn server:app --host 0.0.0.0 --port 8080 --reload
```

## Configuration

Toutes les variables sont configurables via les variables d'environnement :

| Variable | Defaut | Description |
|---|---|---|
| `VLLM_HOST` | `localhost` | Hote des serveurs vLLM |
| `VOXTRAL_PORT` | `8000` | Port vLLM pour Voxtral |
| `VOXTRAL_MODEL` | `mistralai/Voxtral-Mini-4B-Realtime-2602` | Modele Voxtral |
| `QWEN_ASR_PORT` | `8001` | Port vLLM pour Qwen ASR |
| `QWEN_ASR_MODEL` | `Qwen/Qwen3-ASR-1.7B` | Modele Qwen ASR |
| `QWEN_TTS_PORT` | `8002` | Port vLLM pour Qwen TTS |
| `QWEN_TTS_MODEL` | `Qwen/Qwen3-TTS-12Hz-0.6B-Base` | Modele Qwen TTS |

## Architecture

```
server.py          # Point d'entree FastAPI (3 endpoints WS)
voxtral_asr.py     # Classe VoxtralASR (relay vLLM Realtime)
qwen_asr.py        # Classe QwenASR (relay vLLM Realtime)
qwen_tts.py        # Classe QwenTTS (HTTP vers /v1/audio/speech)
```

## Sante du serveur

```bash
curl http://localhost:8080/health
```
