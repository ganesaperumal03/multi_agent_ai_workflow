import redis.asyncio as redis
from app.config import settings
import json

class RedisMemory:

    def __init__(self):
        self.client = redis.from_url(settings.REDIS_URL)

    async def save_session(self, key: str, value: dict):
        await self.client.set(key, json.dumps(value))

    async def get_session(self, key: str):
        data = await self.client.get(key)
        return json.loads(data) if data else None