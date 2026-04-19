from fastapi import APIRouter, HTTPException, Request
from app.models.schemas import AskRequest, AskResponse
from app.services.llm_service import get_llm_response
from app.services.db_service import log_interaction
from app.services.cache_service import get_cached_response, set_cached_response
from app.services.rate_limit_service import check_rate_limit
from app.utils.logger import logger
from app.exceptions import RateLimitExceededError, LLMServiceError

router = APIRouter(tags=["Ask"])


@router.post("/ask", response_model=AskResponse)
def ask_question(request: Request, payload: AskRequest):
    request_id = request.state.request_id
    client_id = request.client.host if request.client else "unknown"

    logger.info(f"Received /ask request | request_id={request_id} | client_id={client_id}")

    try:
        check_rate_limit(client_id)

        cached_result = get_cached_response(payload.question)
        if cached_result:
            logger.info(f"Cache hit | request_id={request_id}")
            log_interaction(
                question=payload.question,
                answer=cached_result["answer"],
                model_used=cached_result["model_used"],
                cached=True,
                request_id=request_id
            )
            return AskResponse(
                answer=cached_result["answer"],
                status="success",
                model_used=cached_result["model_used"],
                source=cached_result["source"],
                cached=True,
                request_id=request_id
            )

        llm_result = get_llm_response(payload.question)
        set_cached_response(payload.question, llm_result)

        log_interaction(
            question=payload.question,
            answer=llm_result["answer"],
            model_used=llm_result["model_used"],
            cached=False,
            request_id=request_id
        )

        return AskResponse(
            answer=llm_result["answer"],
            status="success",
            model_used=llm_result["model_used"],
            source=llm_result["source"],
            cached=False,
            request_id=request_id
        )

    except RateLimitExceededError as e:
        logger.warning(f"Rate limit exceeded | request_id={request_id} | error={e}")
        raise HTTPException(status_code=429, detail=str(e))

    except LLMServiceError as e:
        logger.error(f"LLM service error | request_id={request_id} | error={e}")
        raise HTTPException(status_code=502, detail="LLM provider failed")

    except Exception as e:
        logger.error(f"Unexpected error in /ask | request_id={request_id} | error={e}")
        raise HTTPException(status_code=500, detail="Failed to process question")