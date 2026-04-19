import time
from collections import defaultdict
from app.config import settings
from app.exceptions import RateLimitExceededError

_request_log = defaultdict(list)


def check_rate_limit(client_id: str) -> None:
    now = time.time()
    window_start = now - 60

    recent_requests = [ts for ts in _request_log[client_id] if ts > window_start]
    _request_log[client_id] = recent_requests

    if len(recent_requests) >= settings.RATE_LIMIT_PER_MINUTE:
        raise RateLimitExceededError("Rate limit exceeded. Please try again later.")

    _request_log[client_id].append(now)