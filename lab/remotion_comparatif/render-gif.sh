#!/usr/bin/env bash
set -euo pipefail

# Note: Remotion outputs transparent GIFs if the composition background is transparent.
# We use --still to get the middle frame or render the whole sequence.
# Here we render the sequence.

mkdir -p out

echo "🎬 Rendering ASRComparatif to GIF..."

npx remotion render \
  ASRComparatif \
  out/asr_comparatif.gif \
  --overwrite

echo "✅ Render complete: out/asr_comparatif.gif"
