import redis.asyncio as redis
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")

async def get_redis():
    return await redis.from_url(REDIS_URL, decode_responses=True)
