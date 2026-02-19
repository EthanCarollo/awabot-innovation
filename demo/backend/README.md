# Awabot Demo - Backend AI Services

Ce dossier contient les briques d'intelligence artificielle du projet Awabot, isolees dans des environnements dedies pour eviter les conflits de dependances (notamment sur `transformers`).

## Architecture des Services

Le backend est decompose en 3 services standalone tournant sur des ports distincts :

| Service | Port | Modele | Environnement Conda |
| :--- | :--- | :--- | :--- |
| **Voxtral ASR** | 8082 | `Voxtral-Mini-4B-Realtime` | `awabot-voxtral` |
| **Qwen ASR** | 8083 | `Qwen3-ASR-1.7B` | `awabot-qwen-asr` |
| **Qwen TTS** | 8084 | `Qwen3-TTS-0.6B` | `awabot-qwen-tts` |

## Installation et Lancement Rapide

Le script `manage.sh` automatise la creation des environnements Conda, l'installation des dependances et le lancement des services.

### 1. Lancer les services
```bash
bash manage.sh
```
Le script verifiera si les ports sont deja utilises et vous proposera de tuer les processus existants si necessaire.

### 2. Arreter tous les services
```bash
bash manage.sh stop
```

## Configuration Requise

- **GPU NVIDIA** avec CUDA 12.x recommandé.
- **Conda** installe sur le systeme.
- Environ 12-16 Go de VRAM pour faire tourner les 3 modeles simultanement.

## Structure des dossiers

- `voxtral-asr/` : Transcription temps reel via vLLM.
- `qwen-asr/` : Transcription multilingue via `qwen-asr`.
- `qwen-tts/` : Synthese vocale et clonage de voix via `qwen-tts`.

Chaque service dispose de son propre `server.py` (FastAPI) et `requirements.txt`.
