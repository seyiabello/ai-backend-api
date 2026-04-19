import time
from app.config import settings

_cache = {}


def get_cached_response(question: str):
    item = _cache.get(question)
    if not item:
        return None

    expires_at = item["expires_at"]
    if time.time() > expires_at:
        _cache.pop(question, None)
        return None

    return item["value"]


def set_cached_response(question: str, value: dict):
    _cache[question] = {
        "value": value,
        "expires_at": time.time() + settings.CACHE_TTL_SECONDS
    }