from typing import TypedDict, Optional


class WorkflowState(TypedDict, total=False):
    topic: str
    research: Optional[str]
    generated_code: Optional[str]
    review_feedback: Optional[str]
    refactored_code: Optional[str]
    documentation: Optional[str]