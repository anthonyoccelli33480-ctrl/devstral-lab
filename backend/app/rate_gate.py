"""Rate gate par modèle — zéro 429 sur La Plateforme (free tier ≈ 2–4 req/min)."""

import asyncio
import os
import time

MODEL_INTERVALS: dict[str, float] = {
    "devstral-small-latest": float(os.getenv("DEVSTRAL_RATE_INTERVAL_SEC", "30")),
    "codestral-latest": float(os.getenv("CODESTRAL_RATE_INTERVAL_SEC", "20")),
}

_last: dict[str, float] = {m: 0.0 for m in MODEL_INTERVALS}
_locks: dict[str, asyncio.Lock] = {m: asyncio.Lock() for m in MODEL_INTERVALS}


async def acquire(model: str) -> float:
    if model not in MODEL_INTERVALS:
        model = "devstral-small-latest"
    interval = MODEL_INTERVALS[model]
    async with _locks[model]:
        now = time.monotonic()
        elapsed = now - _last[model]
        wait = max(0.0, interval - elapsed)
        if wait > 0:
            await asyncio.sleep(wait)
        _last[model] = time.monotonic()
        return wait


def next_available_in(model: str | None = None) -> float:
    if model and model in MODEL_INTERVALS:
        return max(0.0, MODEL_INTERVALS[model] - (time.monotonic() - _last[model]))
    return max(
        (max(0.0, iv - (time.monotonic() - _last[m])) for m, iv in MODEL_INTERVALS.items()),
        default=0.0,
    )


def intervals() -> dict[str, float]:
    return dict(MODEL_INTERVALS)