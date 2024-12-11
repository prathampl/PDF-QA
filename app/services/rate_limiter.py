from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from redis import Redis

# Connect to Redis for rate limiting
redis = Redis(host="localhost", port=6379, decode_responses=True)
FastAPILimiter.init(redis)

# Example rate limiter for WebSocket messages
websocket_rate_limit = RateLimiter(times=10, seconds=60)  # 10 messages per minute

async def limit_websocket(user_id: str):
    """
    Enforces rate limiting for WebSocket connections.

    :param user_id: Identifier for the user (e.g., session_id or client IP).
    """
    if not await websocket_rate_limit(user_id):
        raise Exception("Rate limit exceeded. Please wait and try again.")
