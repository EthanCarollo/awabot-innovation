# Backend — Awabot Demo

Serveur FastAPI qui charge et execute les modeles d'IA localement sur GPU.

## Prerequis

> **Important** : Ce backend est concu et optimise pour une inference GPU **NVIDIA (CUDA)**.
> Les modeles utilises ne sont pas compatibles avec Apple MLX, AMD ROCm ou inference CPU.
> Un GPU avec minimum **16 Go de VRAM** est recommande (ex: RTX 4090, A100, L40).

## Endpoints

| Endpoint | Service | Modele | Package |
|---|---|---|---|
| `/ws/voxtral` | Voxtral ASR | `mistralai/Voxtral-Mini-4B-Realtime-2602` | vLLM |
| `/ws/qwen-asr` | Qwen3 ASR | `Qwen/Qwen3-ASR-1.7B` | qwen-asr |
| `/ws/qwen-tts` | Qwen3 TTS | `Qwen/Qwen3-TTS-12Hz-0.6B-Base` | qwen-tts |

## Installation

> `qwen-asr` et `qwen-tts` ont un conflit de version sur `transformers`.
> Utilisez le script d'installation qui gere ce cas :

```bash
bash install.sh
```

## Lancement

```bash
uvicorn server:app --host 0.0.0.0 --port 8082 --reload
```

Les modeles sont charges automatiquement au demarrage du serveur. Le premier lancement
telecharge les poids depuis HuggingFace (~10 Go au total).

## Configuration

| Variable | Defaut | Description |
|---|---|---|
| `DEVICE` | `cuda:0` | GPU a utiliser |
| `VOXTRAL_MODEL` | `mistralai/Voxtral-Mini-4B-Realtime-2602` | Modele Voxtral |
| `QWEN_ASR_MODEL` | `Qwen/Qwen3-ASR-1.7B` | Modele Qwen ASR |
| `QWEN_TTS_MODEL` | `Qwen/Qwen3-TTS-12Hz-0.6B-Base` | Modele Qwen TTS |

## Architecture

```
server.py          # Point d'entree FastAPI, charge les modeles au startup
voxtral_asr.py     # Classe VoxtralASR (inference locale vLLM)
qwen_asr.py        # Classe QwenASR (inference locale qwen-asr)
qwen_tts.py        # Classe QwenTTS (inference locale qwen-tts)
```

## Sante du serveur

```bash
curl http://localhost:8082/health
```

Retourne le statut de chaque modele (charge ou non).
