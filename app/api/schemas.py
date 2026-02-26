from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


# ==============================
# Request Model
# ==============================

class WorkflowRequest(BaseModel):
    topic: str = Field(..., example="Design scalable FastAPI microservice")
    workflow_engine: Optional[str] = Field(
        default=None,
        example="langgraph",
        description="Override workflow engine (langgraph or crewai)"
    )


# ==============================
# Evaluation Score Model
# ==============================

class EvaluationScore(BaseModel):
    quality: int
    clarity: int
    completeness: int
    maintainability: int
    overall_score: float


# ==============================
# Workflow Response Model
# ==============================

class WorkflowResponse(BaseModel):
    research: Optional[str]
    code: Optional[Dict[str, Any]]
    review: Optional[Dict[str, Any]]
    refactor: Optional[Dict[str, Any]]
    documentation: Optional[Dict[str, Any]]
    evaluation_score: Optional[EvaluationScore]