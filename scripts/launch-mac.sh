#!/bin/bash
set -euo pipefail

PROJECT="/Users/anthonyoccelli/projects/devstral-lab"
LOG_DIR="$HOME/Library/Logs/Devstral Lab"
FRONT_URL="http://127.0.0.1:5175"

mkdir -p "$LOG_DIR"
port_in_use() { lsof -iTCP:"$1" -sTCP:LISTEN -t >/dev/null 2>&1; }
http_ready() { curl -sf --max-time 2 "$1" >/dev/null 2>&1; }

echo ""; echo "  🧪 Devstral Lab — démarrage"; echo ""

if [[ ! -x "$PROJECT/backend/.venv/bin/uvicorn" ]]; then
  (cd "$PROJECT" && make install)
fi

if port_in_use 8788 && http_ready "http://127.0.0.1:8788/api/health"; then
  echo "  ✓ Backend (:8788)"
else
  echo "  → Backend…"
  (cd "$PROJECT/backend" && nohup .venv/bin/uvicorn app.main:app --reload --host 127.0.0.1 --port 8788 >>"$LOG_DIR/backend.log" 2>&1 &)
  for _ in $(seq 1 60); do http_ready "http://127.0.0.1:8788/api/health" && break; sleep 0.5; done
fi

if http_ready "$FRONT_URL"; then
  echo "  ✓ Frontend ($FRONT_URL)"
else
  echo "  → Frontend…"
  (cd "$PROJECT/frontend" && nohup npm run dev >>"$LOG_DIR/frontend.log" 2>&1 &)
  for port in 5175 5176; do
    for _ in $(seq 1 60); do
      if http_ready "http://127.0.0.1:$port/"; then FRONT_URL="http://127.0.0.1:$port"; break 2; fi
      sleep 0.5
    done
  done
fi

HEALTH=$(curl -sf "http://127.0.0.1:8788/api/health" 2>/dev/null || true)
if echo "$HEALTH" | grep -q '"mistral_key": true'; then
  echo "  ✓ Mistral connecté"
else
  echo "  ○ Configure la clé dans l'onboarding"
fi

echo "  → $FRONT_URL"
open "$FRONT_URL"
echo ""; echo "  Appuyez sur Entrée pour fermer (serveurs restent actifs)."; read -r _