"""Database session and engine configuration."""
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# 1. Create the asynchronous database engine
# Echo=True logs all generated SQL statements to your terminal (great for development)
async_engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=True,
    future=True,
    pool_pre_ping=True,  # Automatically detects and recovers dropped connections
    pool_size=10,        # Maximum number of persistent connections to keep open
    max_overflow=20      # Maximum number of temporary connections allowed during surges
)

# 2. Create an explicit session factory bound to our async engine
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Prevents SQLAlchemy from doing unneeded lazy-loads after commit
    autocommit=False,
    autoflush=False
)


# 3. Dependency Injector for your API Routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that yields an active async database session.
    Guarantees the session is properly closed after a request finishes,
    even if an unexpected error occurs during processing.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()