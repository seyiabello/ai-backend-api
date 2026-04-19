import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "AI Backend API"
    APP_VERSION: str = "1.2.0"
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./interactions.db")
    CACHE_TTL_SECONDS: int = int(os.getenv("CACHE_TTL_SECONDS", "300"))
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "5"))


settings = Settings()