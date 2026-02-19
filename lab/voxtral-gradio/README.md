# 🎙️<p align="center">
  <img src="../../website/public/logo_baseline.svg" width="300" alt="Awabot Logo">
</p>

# Voxtral Gradio Prototype
 Caméra + Transcription

Prototype rapide pour tester **Voxtral Mini 4B Realtime** avec :
- 📹 Retour caméra en direct
- 📝 Transcription temps-réel en overlay (sous-titres)

## Prérequis

- **GPU NVIDIA** avec ≥ 16 Go VRAM (RTX 4090, A100, etc.)
- **Conda** installé
- Webcam + Micro

## Installation

```bash
# 1. Créer l'env conda
conda env create -f environment.yml

# 2. Activer l'env
conda activate voxtral

# 3. (Optionnel) Vérifier que mistral_common est bien installé
python -c "import mistral_common; print(mistral_common.__version__)"
```

## Utilisation

### Étape 1 — Lancer le serveur vLLM

```bash
# Le modèle sera téléchargé automatiquement au premier lancement (~8 Go)
bash serve.sh
```

> Attendre que le log affiche `Route: /v1/realtime, Endpoint: realtime_endpoint`

### Étape 2 — Lancer l'app

```bash
python app.py --host localhost --port 8000
```

Options :
| Flag | Description | Default |
|------|-------------|---------|
| `--host` | Hôte du serveur vLLM | `localhost` |
| `--port` | Port du serveur vLLM | `8000` |
| `--camera` | Index de la caméra | `0` |
| `--share` | Créer un lien Gradio public | `false` |
| `--model` | Modèle vLLM (si différent) | `mistralai/Voxtral-Mini-4B-Realtime-2602` |

### Résultat

L'interface Gradio s'ouvre dans le navigateur :
1. Cliquer **▶ Start**
2. Parler dans le micro → la transcription apparaît en sous-titres sur le flux caméra
3. Cliquer **⏹ Stop** pour arrêter

## Architecture

```
voxtral/
├── environment.yml   # Env conda
├── serve.sh          # Script de lancement vLLM
├── app.py            # App Gradio (caméra + transcription)
└── README.md         # Ce fichier
```

```
┌──────────┐   audio (ws)   ┌───────────────┐
│  Micro   │ ─────────────► │  vLLM Server  │
│  + Cam   │ ◄───────────── │  (Voxtral 4B) │
└──────────┘  transcription └───────────────┘
      │
      ▼
 ┌──────────────────────┐
 │  Gradio UI           │
 │  Cam + Sous-titres   │
 └──────────────────────┘
```

## Liens

- [Voxtral Mini 4B Realtime (HuggingFace)](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- [vLLM Realtime API docs](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/?h=realtime#realtime-api)
- [Demo officielle](https://huggingface.co/spaces/mistralai/Voxtral-Mini-Realtime)
