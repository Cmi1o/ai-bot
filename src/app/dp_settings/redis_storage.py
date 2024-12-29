import redis.asyncio as aioredis

from config import redis_url

storage = aioredis.from_url(redis_url)
