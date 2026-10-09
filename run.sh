#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -f filedrawer.setup.yaml ]; then
  echo "Choose the models, review and options first: filedrawer configure ." >&2
  exit 1
fi
if ! grep -q '^provider: local' filedrawer.setup.yaml; then
  : "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY (bring your own token)}"
fi
filedrawer run --csv inputs/export.csv --qsf inputs/survey.qsf --pap inputs/pap.md \
  --slug "scientific-trust-messages" --title "Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages" --authors "Yamil R. Velez" --repo-url "https://github.com/yrvelez/scientific-trust-messages" \
  --package-dir . "$@"
