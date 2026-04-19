from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


@patch("app.routes.ask.check_rate_limit")
@patch("app.routes.ask.get_cached_response")
@patch("app.routes.ask.get_llm_response")
@patch("app.routes.ask.set_cached_response")
@patch("app.routes.ask.log_interaction")
def test_ask_endpoint_success(
    mock_log_interaction,
    mock_set_cached_response,
    mock_get_llm_response,
    mock_get_cached_response,
    mock_check_rate_limit
):
    mock_get_cached_response.return_value = None
    mock_get_llm_response.return_value = {
        "answer": "RAG stands for Retrieval Augmented Generation.",
        "model_used": "gpt-4.1-mini",
        "source": "openai"
    }

    payload = {"question": "What is RAG?"}
    response = client.post("/ask", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["cached"] is False
    assert "request_id" in data


@patch("app.routes.ask.check_rate_limit")
@patch("app.routes.ask.get_cached_response")
@patch("app.routes.ask.log_interaction")
def test_ask_endpoint_cache_hit(
    mock_log_interaction,
    mock_get_cached_response,
    mock_check_rate_limit
):
    mock_get_cached_response.return_value = {
        "answer": "Cached answer.",
        "model_used": "gpt-4.1-mini",
        "source": "openai"
    }

    payload = {"question": "What is RAG?"}
    response = client.post("/ask", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["cached"] is True
    assert data["answer"] == "Cached answer."