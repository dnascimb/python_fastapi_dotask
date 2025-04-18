import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS random_numbers (
            id SERIAL PRIMARY KEY,
            value INTEGER NOT NULL
        )
    """)
    return conn
