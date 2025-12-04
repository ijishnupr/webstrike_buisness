import os
import psycopg
from psycopg_pool import AsyncConnectionPool
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

pool = AsyncConnectionPool(
    conninfo=DATABASE_URL,
    open=False,          # start pool manually
    max_size=10,         # number of connections
)

async def get_connection():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            yield conn, cur