from fastapi import APIRouter, HTTPException, Request
from app.models.schemas import FeedbackRequest, FeedbackResponse
from app.services.db_service import log_feedback
from app.utils.logger import logger

router = APIRouter(tags=["Feedback"])


@router.post("/feedback", response_model=FeedbackResponse)
def submit_feedback(request: Request, payload: FeedbackRequest):
    request_id = request.state.request_id
    logger.info(f"Received /feedback request | request_id={request_id}")

    try:
        log_feedback(
            question=payload.question,
            answer=payload.answer,
            rating=payload.rating,
            request_id=request_id
        )
        return FeedbackResponse(
            status="success",
            message="Feedback received",
            request_id=request_id
        )
    except Exception as e:
        logger.error(f"Error in /feedback endpoint | request_id={request_id} | error={e}")
        raise HTTPException(status_code=500, detail="Failed to save feedback")