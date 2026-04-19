from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_feedback_endpoint():
    payload = {
        "question": "What is RAG?",
        "answer": "RAG stands for Retrieval Augmented Generation.",
        "rating": 5
    }

    response = client.post("/feedback", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"] == "Feedback received"
    assert "request_id" in data