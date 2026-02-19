#!/usr/bin/env bash
# ──────────────────────────────────────────────
# Lancer le serveur vLLM pour Voxtral Realtime
# Requiert un GPU avec >= 16 Go VRAM
# ──────────────────────────────────────────────
set -euo pipefail

MODEL="mistralai/Voxtral-Mini-4B-Realtime-2602"
HOST="${VLLM_HOST:-0.0.0.0}"
PORT="${VLLM_PORT:-8000}"

echo "🚀 Démarrage vLLM — modèle: $MODEL"
echo "   Endpoint Realtime: ws://$HOST:$PORT/v1/realtime"

VLLM_DISABLE_COMPILE_CACHE=1 vllm serve "$MODEL" \
    --host "$HOST" \
    --port "$PORT" \
    --compilation_config '{"cudagraph_mode": "PIECEWISE"}' \
    "$@"
