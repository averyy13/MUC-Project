from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from app.core.config import settings
from app.db.session import engine
from app.api.v1.routers.spatial import router as spatial_router
from app.api.v1.routers.emergency_categories import router as emergency_category_router
from app.api.v1.routers.auth import router as auth_router
from app.api.v1.routers.admin import router as admin_router
from app.api.v1.routers.volunteers import router as volunteer_router
from app.api.v1.routers.emergency_requests import router as emergency_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts and once when it shuts down.
    Used here to verify database connectivity.
    """

    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("Database connection established.")
    except Exception as e:
        print(f"Database connection failed: {e}")

    yield

    await engine.dispose()
    print("Database connection closed.")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    lifespan=lifespan,
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Emergency Medical Assistant API",
        "status": "running",
    }

@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
    }
    
app.include_router(
    emergency_category_router,
    prefix="/api/v1",
)  
app.include_router(
    auth_router,
    prefix="/api/v1"
)
app.include_router(
    admin_router,
    prefix="/api/v1"
)
app.include_router(
    volunteer_router,
    prefix="/api/v1",
)
app.include_router(
    spatial_router,
    prefix="/api/v1",
)