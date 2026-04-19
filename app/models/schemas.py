from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User question")


class AskResponse(BaseModel):
    answer: str
    status: str
    model_used: str
    source: str


from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User question")


class AskResponse(BaseModel):
    answer: str
    status: str
    model_used: str
    source: str
    cached: bool
    request_id: str


class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int = Field(..., ge=1, le=5)


class FeedbackResponse(BaseModel):
    status: str
    message: str
    request_id: str


class HealthResponse(BaseModel):
    status: str
    message: str
    version: str


class DetailedHealthResponse(BaseModel):
    status: str
    message: str
    version: str
    database: str
    model: str