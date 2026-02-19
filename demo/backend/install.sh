#!/bin/bash
# install.sh — Installe les deps du backend demo Awabot
# Usage: bash install.sh
#
# Note: qwen-asr et qwen-tts ont un conflit de version
# sur transformers (4.57.6 vs 4.57.3). On installe les
# wrappers sans deps puis on pin transformers manuellement.

set -e

echo "Installation des deps de base…"
pip install fastapi "uvicorn[standard]" torch numpy soundfile

echo "Installation de qwen-asr (sans deps)…"
pip install --no-deps qwen-asr

echo "Installation de qwen-tts (sans deps)…"
pip install --no-deps qwen-tts

echo "Installation de transformers (version compatible)…"
pip install "transformers>=4.57.3"

echo "Installation de vllm…"
pip install vllm

echo "Installation terminee."
