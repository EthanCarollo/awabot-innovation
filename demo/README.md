# Voxtral Realtime Demo

Transcription audio en temps réel via **Voxtral Mini 4B** (vLLM Realtime API).

## Architecture

```
Browser (Nuxt, port 3001)
  ↕ WebSocket (audio PCM16 b64)
Python Backend (FastAPI, port 8080)
  ↕ WebSocket (vLLM Realtime API)
vLLM Server (port 8000)
```

## Lancement

### 1. Serveur vLLM (GPU requis)

```bash
cd lab/voxtral-gradio
bash serve.sh
```

### 2. Backend Python

```bash
cd demo/backend
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8080 --reload
```

### 3. Frontend Nuxt

```bash
cd demo/frontend
npm install
npm run dev -- --port 3001
```

Ouvrir [http://localhost:3001](http://localhost:3001), cliquer **Démarrer** et parler.

## Configuration

| Variable | Défaut | Description |
|---|---|---|
| `VLLM_HOST` | `localhost` | Hôte du serveur vLLM |
| `VLLM_PORT` | `8000` | Port du serveur vLLM |
| `VLLM_MODEL` | `mistralai/Voxtral-Mini-4B-Realtime-2602` | Modèle servi |
| `WS_BACKEND_URL` | `ws://localhost:8080/ws/transcribe` | URL WebSocket backend (côté Nuxt) |
