"""Application entry point for the Emergency Medical Assistant API."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from app.database.session import async_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the server boots up
    print("Connecting to PostgreSQL...")
    try:
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print(" SUCCESS: FastAPI successfully connected to PostgreSQL!")
    except Exception as e:
        print(f" FAILURE: Database connection failed. Error: {e}")
    yield
    # This runs when the server shuts down

app = FastAPI(title="Emergency Management API", lifespan=lifespan)