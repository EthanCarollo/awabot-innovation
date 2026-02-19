#!/usr/bin/env bash
set -euo pipefail

mkdir -p out

echo "🖼️  Rendering ASRComparatif to PNG (last frame) - 1080p..."

npx remotion still \
  ASRComparatif \
  out/asr_comparatif.png \
  --frame 60 \
  --overwrite

echo "✅ Render complete: out/asr_comparatif.png"
