<p align="center">
  <img src="website/public/logo_baseline.svg" alt="Awabot" height="80" />
</p>

<h3 align="center">Awabot Innovation — Téléprésence Intelligente</h3>

<p align="center">
  <a href="https://github.com/EthanCarollo/awabot-innovation"><img alt="GitHub" src="https://img.shields.io/badge/github-awabot--innovation-orange?logo=github&style=flat-square" /></a>
</p>

---

## Structure du Projet

```
awabot/
├── website/          # Site vitrine Nuxt.js + Cahier des Charges
├── demo/             # Démo Voxtral Realtime (Nuxt + Python WS)
│   ├── backend/      # Serveur FastAPI (relais WebSocket vers vLLM)
│   └── frontend/     # Interface Nuxt.js (capture micro + transcription)
└── lab/              # Expérimentations & Prototypes
    ├── voxtral-gradio/    # Prototype Gradio Voxtral + Caméra
    ├── remotion_comparatif/ # Vidéo comparative ASR (Remotion)
    └── realbench/         # Benchmarks temps réel
```

## Website

Site vitrine Awabot avec le **Cahier des Charges** interactif.

```bash
cd website
npm install
npm run dev -- --port 3000
```

> Accessible sur [http://localhost:3000](http://localhost:3000)
> Cahier des Charges sur [http://localhost:3000/cdc](http://localhost:3000/cdc)

## Demo — Voxtral Realtime

Démo de transcription audio temps réel via **Voxtral Mini 4B** (vLLM Realtime API).

### Backend (Python)

```bash
cd demo/backend
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8080 --reload
```

### Frontend (Nuxt)

```bash
cd demo/frontend
npm install
npm run dev -- --port 3001
```

> Requiert un serveur vLLM actif avec Voxtral (`bash lab/voxtral-gradio/serve.sh`)

## Lab — Expérimentations

| Dossier | Description |
|---|---|
| `voxtral-gradio/` | Prototype Gradio: webcam + transcription temps réel |
| `remotion_comparatif/` | Vidéo de comparaison des modèles ASR |
| `realbench/` | Benchmarks de performance en conditions réelles |

## Stack Technique

- **Frontend** — [Nuxt.js](https://nuxt.com/) + [TailwindCSS](https://tailwindcss.com/)
- **Backend** — [Django REST Framework](https://www.django-rest-framework.org/) + [FastAPI](https://fastapi.tiangolo.com/)
- **ASR** — [Voxtral](https://mistral.ai/) + [Qwen3-ASR](https://github.com/QwenLM/Qwen-Audio)
- **Traduction** — [HY-MT](https://huggingface.co/tencent/HY-MT1.5-1.8B) / [Gemma Translate](https://huggingface.co/google/translategemma-4b-it) / [LibreTranslate](https://fr.libretranslate.com/)
- **TTS** — [Qwen3-TTS](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base)
- **Inférence** — [vLLM](https://vllm.ai/)
- **Analytics** — [Umami](https://umami.is/) ([guide de setup](UMAMI.md))
