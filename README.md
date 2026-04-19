<!-- ======================= -->
<!-- HERO SECTION -->
<!-- ======================= -->

<h1 align="center">AI Backend API</h1>

<p align="center">
  <b>Production-style AI backend with FastAPI, OpenAI, caching, rate limiting, and Docker</b>
</p>

<p align="center">
  Built to simulate real-world AI system architecture beyond simple demos
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/OpenAI-LLM-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Docker-Containerised-2496ED?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Pytest-Tested-success?style=for-the-badge"/>
</p>

---

## Overview

This project is a **production-style AI backend** that exposes LLM functionality via a structured API.

Unlike simple AI demos, this system includes:

- Request tracing
- Structured responses
- Caching for cost/performance optimisation
- Rate limiting for protection
- Persistent logging
- Test coverage
- Docker containerisation

---

## Features

### Core AI Functionality
- LLM-powered `/ask` endpoint using OpenAI API
- Structured JSON responses for reliability
- Prompt-controlled outputs

### Production-Minded Features
- **Caching layer** — reduces cost and improves latency
- **Rate limiting** — protects API from abuse
- **Request ID tracing** — debugging and observability
- **SQLite logging** — interactions and feedback
- **Pytest test suite**
- **Dockerised deployment**

---

## Architecture

```
Client → FastAPI → Services Layer → OpenAI API
                       ↓
                  Cache Layer
                       ↓
               Database (SQLite)
```

---

## API Endpoints

| Endpoint         | Method | Description          |
|------------------|--------|----------------------|
| `/health`        | GET    | Basic health check   |
| `/health/details`| GET    | Detailed system info |
| `/ask`           | POST   | Query LLM            |
| `/feedback`      | POST   | Store feedback       |

### Example Request

```json
{
  "question": "What is retrieval augmented generation?"
}
```

### Example Response

```json
{
  "answer": "RAG stands for Retrieval Augmented Generation...",
  "status": "success",
  "model_used": "gpt-4.1-mini",
  "source": "openai",
  "cached": false,
  "request_id": "abc123"
}
```

---

## Key Engineering Concepts Demonstrated

- API-first AI system design
- LLM integration via SDKs
- Structured outputs (not raw text)
- Caching strategies
- Rate limiting
- Logging and traceability
- Test-driven backend development
- Containerisation

---

## Tech Stack

- Python
- FastAPI
- OpenAI API
- SQLite / SQLAlchemy
- Pytest
- Docker

---

## Running the Project

### 1. Clone

```bash
git clone https://github.com/yourusername/ai-backend-api.git
cd ai-backend-api
```

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Run locally

```bash
uvicorn app.main:app --reload
```

Open: [http://localhost:8000/docs](http://localhost:8000/docs)

### 4. Run tests

```bash
pytest
```

### 5. Run with Docker

```bash
docker build -t ai-backend-api .
docker run -p 8000:8000 --env-file .env ai-backend-api
```

---

## Environment Variables

```env
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4.1-mini
DATABASE_URL=sqlite:///./interactions.db
CACHE_TTL_SECONDS=300
RATE_LIMIT_PER_MINUTE=5
```

---

## What This Project Shows

This project demonstrates the ability to:

- Build real AI-backed APIs
- Design production-aware systems
- Optimise cost and performance
- Structure backend services cleanly
- Move beyond basic AI demos

---

## Next Steps

Planned improvements:

- RAG system with document upload
- Vector database integration
- Advanced evaluation pipeline
- Monitoring and observability (Prometheus/Grafana)

---

## Author

**Oluwaseyi Bello**  
AI Engineer | MLOps | Intelligent Systems
