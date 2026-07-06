<div align="center">

# 🧪 Devstral Lab

**14 one-shot coding agents on [Mistral La Plateforme](https://docs.mistral.ai) — Devstral Small 2 + Codestral, zero-429 by design.**

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Agents](https://img.shields.io/badge/agents-14-orange.svg)](#agents)
[![Mistral](https://img.shields.io/badge/Mistral-La_Plateforme-ff7000)](https://console.mistral.ai)

*Phase 1 of the Mistral showcase stack · [Mistral Bureau](docs/ROADMAP.md) comes next.*

</div>

## What is this?

Open-source **code agentic** showcase for Mistral's specialized models:

| Model | Agents | Rate gate |
|-------|--------|-----------|
| **Devstral Small 2** | Review, Fix, Impl, Refactor, Test, Explain, Migrate, Secret | 30s |
| **Codestral** | Commit, Regex, SQL, Docker, OpenAPI, API Design | 20s |

One task → one call → structured JSON. No LangChain. No agent loops.

## Quick start

```bash
cd devstral-lab
cp .env.example .env   # MISTRAL_API_KEY from console.mistral.ai

make install
make backend   # :8788
make frontend  # :5175
```

## Agents

**Devstral (agentic)** — Lab Review · Lab Fix · Lab Impl · Lab Refactor · Lab Explain · Lab Test · Lab Migrate · Lab Secret

**Codestral** — Lab Commit · Lab Regex · Lab SQL · Lab Docker · Lab OpenAPI · Lab API Design

## Architecture

```
React UI → FastAPI → RateGate (per model) → api.mistral.ai → JSON
```

## Roadmap

1. ✅ **Devstral Lab** (this repo) — code agents
2. 🔜 **Mistral Bureau** — FR multi-model (Large, Pixtral, OCR, career)

## License

MIT