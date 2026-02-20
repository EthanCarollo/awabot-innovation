<p align="center">
  <img src="website/public/logo_baseline.svg" width="400" alt="Awabot Logo">
</p>

# Awabot Innovation — Téléprésence & IA Souveraine

[![GitHub](https://img.shields.io/badge/github-awabot--innovation-orange?logo=github&style=flat-square)](https://github.com/EthanCarollo/awabot-innovation)

> [!NOTE]
> **Contexte du Projet :** Ce travail est réalisé dans le cadre d'un **Workshop d'Innovation** au sein de l'école **by CCI Gobelins Annecy**. L'objectif principal est de formuler une proposition d'innovation concrète et technique basée sur un concept de téléprésence donné.

Ce dépôt centralise les travaux de recherche, de prototypage et de spécification technique pour la **nouvelle génération d'interfaces Awabot**. L'objectif est de transformer la téléprésence robotique en une expérience immersive, accessible et intelligente, tout en garantissant une **souveraineté totale des données**.

---

## Vision & Concept

Nous construisons une plateforme de **tourisme immersif à distance**. Un utilisateur peut piloter un robot Awabot dans un lieu culturel (musée, monument) tout en bénéficiant :
- **D'une interface Full Web** moderne et réactive (Nuxt.js).
- **D'une intelligence artificielle embarquée** pour la transcription (ASR), la traduction (NMT) et la synthèse vocale (TTS).
- **D'une accessibilité universelle**, pensée pour l'inclusion sociale des personnes à mobilité réduite ou isolées.

---

## Architecture du Projet

```
awabot/
├── website/          # Platforme Nuxt.js + Spécifications (CDC)
├── demo/             # Démonstrateurs Temps Réel (ASR/TTS)
│   ├── backend/      # Relais WebSocket vers serveurs d'inférence
│   └── frontend/     # Cockpit de pilotage & transcription
└── lab/              # Laboratoire R&D
    ├── voxtral-gradio/    # POC Inférence Mistral/Voxtral
    ├── remotion_comparatif/ # Visualisation de data & benchmarks
    └── realbench/         # Mesures de latence & WER
```

---

## Le Moteur d'Interaction (Stack IA)

Notre architecture repose sur des modèles **Open-Weight** auto-hébergés via **vLLM** pour une confidentialité et une latence minimales.

### Transcription (ASR)
- **Modèles :** [Voxtral Mini 4B](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) (Optimal FR/EU) & [Qwen3-ASR](https://github.com/QwenLM/Qwen-Audio) (Optimal EN/ZH).
- **Performance :** Latence configurable à partir de 80ms.

### Traduction (NMT)
- **Choix MVP :** [LibreTranslate](https://fr.libretranslate.com/) (Open-source, gratuit, déploiement simple).
- **Alternatives LLM :** HY-MT, Gemma Translate pour une correction contextuelle avancée.

### Synthèse Vocale (TTS)
- **Modèle :** [Qwen3-TTS-0.6B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base).
- **Capacité :** Clonage de voix en temps réel sur infrastructure standard.

---

## Documentation & Ressources

Le projet est régi par un **Cahier des Charges (CDC)** vivant qui documente les choix stratégiques et techniques.
- **Accès direct :** [website/content/cdc.md](website/content/cdc.md) (ou via l'interface web locale).
- **Benchmarks :** Résultats détaillés dans le dossier `lab/realbench`.
- **Analytics :** Infrastructure [Umami](https://umami.is/) pour le suivi respectueux (voir [UMAMI.md](UMAMI.md)).

---

## Démarrage Rapide

### 1. Website & Documentation
```bash
cd website
npm install && npm run dev
```

### 2. Démo ASR Voxtral
```bash
# Backend (Inférence & WS)
cd demo/backend
pip install -r requirements.txt && python server.py

# Frontend (Capture & UI)
cd demo/frontend
npm install && npm run dev
```

---

<p align="center">
  <i>Awabot Innovation — Connecter les humains, par-delà les frontières.</i>
</p>
