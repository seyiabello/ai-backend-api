from fastapi import APIRouter
from app.models.schemas import HealthResponse, DetailedHealthResponse
from app.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        message="API is running",
        version=settings.APP_VERSION
    )


@router.get("/health/details", response_model=DetailedHealthResponse)
def detailed_health_check():
    return DetailedHealthResponse(
        status="ok",
        message="Detailed health check passed",
        version=settings.APP_VERSION,
        database=settings.DATABASE_URL,
        model=settings.OPENAI_MODEL
    )