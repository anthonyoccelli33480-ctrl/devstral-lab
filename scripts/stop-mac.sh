#!/bin/bash
for port in 8788 5175 5176; do
  pids=$(lsof -tiTCP:"$port" -sTCP:LISTEN 2>/dev/null || true)
  [[ -n "$pids" ]] && kill $pids 2>/dev/null || true
done
echo "  ✓ Devstral Lab arrêté"
read -r _