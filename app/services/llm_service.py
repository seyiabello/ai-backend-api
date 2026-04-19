from openai import OpenAI
from app.config import settings
from app.utils.logger import logger
from app.exceptions import LLMServiceError

if not settings.OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing from environment variables")

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_llm_response(question: str) -> dict:
    prompt = f"""
You are a helpful AI assistant.
Answer the user's question clearly, accurately, and concisely.
If the question is ambiguous, say so.
Return a plain-text answer only.

User question: {question}
"""

    try:
        logger.info("Sending request to LLM")
        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt
        )
        answer = response.output_text.strip()

        logger.info("LLM response received successfully")
        return {
            "answer": answer,
            "model_used": settings.OPENAI_MODEL,
            "source": "openai"
        }

    except Exception as e:
        logger.error(f"LLM API call failed: {e}")
        raise LLMServiceError(f"LLM API call failed: {e}")