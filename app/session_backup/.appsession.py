import uuid
import json
from datetime import timedelta
import redis.asyncio as aioredis

REDIS_URL = "redis://localhost:6379/0"
SESSION_TTL_SECONDS = 60 * 60 * 24  # 24 ore

redis_client = aioredis.from_url(REDIS_URL, decode_responses=True)

async def create_session(data: dict) -> str:
    sid = str(uuid.uuid4())
    await redis_client.setex(f"session:{sid}", SESSION_TTL_SECONDS, json.dumps(data))
    return sid

async def get_session(sid: str) -> dict | None:
    raw = await redis_client.get(f"session:{sid}")
    if not raw:
        return None
    return json.loads(raw)

async def delete_session(sid: str) -> None:
    await redis_client.delete(f"session:{sid}")
