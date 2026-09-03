from functools import lru_cache
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Application
    APP_NAME: str = "Emergency Medical Assistant API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # PostgreSQL
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # Google API
    GOOGLE_ROUTES_API_KEY: str
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str = "google/gemma-4-31b-it:free"

    # Firebase
    FCM_PROJECT_ID: str | None = None
    FCM_CLIENT_EMAIL: str | None = None
    FCM_PRIVATE_KEY: str | None = None
    FIREBASE_CREDENTIALS_PATH: str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        password = quote_plus(self.POSTGRES_PASSWORD)

        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{password}@"
            f"{self.POSTGRES_SERVER}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()

