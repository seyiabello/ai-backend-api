from fastapi import FastAPI
from app.config import settings
from app.middleware import RequestIDMiddleware
from app.routes.health import router as health_router
from app.routes.ask import router as ask_router
from app.routes.feedback import router as feedback_router

app = FastAPI(
    title=settings.APP_NAME,
    description="A production-style AI backend built with FastAPI, OpenAI, SQLite, Docker, caching, and rate limiting",
    version=settings.APP_VERSION
)

app.add_middleware(RequestIDMiddleware)

app.include_router(health_router)
app.include_router(ask_router)
app.include_router(feedback_router)


@app.get("/")
def root():
    return {
        "message": "AI Backend API is running",
        "docs": "/docs",
        "health": "/health"
    }