from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func
from app.database.db_session import Base


class WorkflowRun(Base):
    __tablename__ = "workflow_runs"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)

    research = Column(Text)
    generated_code = Column(Text)
    review_feedback = Column(Text)
    refactored_code = Column(Text)
    documentation = Column(Text)

    quality_score = Column(Integer)
    clarity_score = Column(Integer)
    completeness_score = Column(Integer)
    maintainability_score = Column(Integer)
    overall_score = Column(Float)

    created_at = Column(DateTime(timezone=True), server_default=func.now())