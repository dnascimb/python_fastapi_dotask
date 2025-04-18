from fastapi import FastAPI
import random
import logging

from .db import init_db
from .cache import get_redis

app = FastAPI()
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


@app.post("/tasks")
async def run_task():
    logger.info("Task triggered")

    rand_value = random.randint(1, 1000)
    logger.info(f"Generated random number: {rand_value}")

    # Save to Postgres
    conn = await init_db()
    await conn.execute("INSERT INTO random_numbers(value) VALUES($1)", rand_value)
    await conn.close()
    logger.info("Saved to Postgres")

    # Save to Redis with TTL
    redis = await get_redis()
    await redis.set("latest_random", rand_value, ex=60)
    logger.info("Saved to Redis with TTL 60s")

    return {"status": "success", "value": rand_value}


@app.get("/health")
async def health():
    checks = {}

    try:
        conn = await init_db()
        await conn.execute("SELECT 1")
        await conn.close()
        checks["postgres"] = "ok"
    except Exception as e:
        logger.exception("Postgres health check failed")
        checks["postgres"] = "error"

    try:
        redis = await get_redis()
        pong = await redis.ping()
        checks["redis"] = "ok" if pong else "error"
    except Exception as e:
        logger.exception("Redis health check failed")
        checks["redis"] = "error"

    status = "ok" if all(v == "ok" for v in checks.values()) else "error"
    return {"status": status, "checks": checks}
