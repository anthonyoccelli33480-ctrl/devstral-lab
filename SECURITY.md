# Security

- `MISTRAL_API_KEY` in `.env` only (gitignored, chmod 600)
- Never commit keys or paste in issues
- FastAPI proxies all Mistral calls — key never in browser after onboarding