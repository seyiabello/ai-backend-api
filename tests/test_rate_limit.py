from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.exceptions import RateLimitExceededError

client = TestClient(app)


@patch("app.routes.ask.check_rate_limit")
def test_rate_limit_exceeded(mock_check_rate_limit):
    mock_check_rate_limit.side_effect = RateLimitExceededError(
        "Rate limit exceeded. Please try again later."
    )

    payload = {"question": "What is AI engineering?"}
    response = client.post("/ask", json=payload)

    assert response.status_code == 429
    data = response.json()
    assert data["detail"] == "Rate limit exceeded. Please try again later."