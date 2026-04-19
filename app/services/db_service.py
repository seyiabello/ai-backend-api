from datetime import datetime
from app.models.database import SessionLocal, Interaction, Feedback
from app.utils.logger import logger


def log_interaction(
    question: str,
    answer: str,
    model_used: str,
    cached: bool,
    request_id: str
) -> None:
    db = SessionLocal()
    try:
        interaction = Interaction(
            question=question,
            answer=answer,
            model_used=model_used,
            cached=cached,
            request_id=request_id,
            timestamp=datetime.utcnow().isoformat()
        )
        db.add(interaction)
        db.commit()
        logger.info(f"Interaction logged successfully | request_id={request_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to log interaction | request_id={request_id} | error={e}")
        raise
    finally:
        db.close()


def log_feedback(question: str, answer: str, rating: int, request_id: str) -> None:
    db = SessionLocal()
    try:
        feedback = Feedback(
            question=question,
            answer=answer,
            rating=rating,
            request_id=request_id,
            timestamp=datetime.utcnow().isoformat()
        )
        db.add(feedback)
        db.commit()
        logger.info(f"Feedback logged successfully | request_id={request_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to log feedback | request_id={request_id} | error={e}")
        raise
    finally:
        db.close()