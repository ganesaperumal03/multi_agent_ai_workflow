from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import WorkflowRun


def _safe_nested_get(data: dict, key: str, subkey: str):
    """Safely get a value from a nested dict, returning None if not possible."""
    value = data.get(key)
    if isinstance(value, dict):
        return value.get(subkey)
    return None


async def create_workflow_run(
    db: AsyncSession,
    topic: str,
    result: dict,
):
    eval_score = result.get("evaluation_score", {}) or {}

    # Handle both LangGraph (nested dicts) and CrewAI (flat crewai_output) formats
    crewai_output = result.get("crewai_output")
    if crewai_output is not None:
        # CrewAI format: single output string, no per-agent breakdown
        output_str = str(crewai_output)
        research = output_str
        generated_code = None
        review_feedback = None
        refactored_code = None
        documentation = None
    else:
        # LangGraph format: nested dicts per agent
        research = _safe_nested_get(result, "research", "research")
        generated_code = _safe_nested_get(result, "code", "generated_code")
        review_feedback = _safe_nested_get(result, "review", "review_feedback")
        refactored_code = _safe_nested_get(result, "refactor", "refactored_code")
        documentation = _safe_nested_get(result, "documentation", "documentation")

    workflow = WorkflowRun(
        topic=topic,
        research=research,
        generated_code=generated_code,
        review_feedback=review_feedback,
        refactored_code=refactored_code,
        documentation=documentation,
        quality_score=eval_score.get("quality"),
        clarity_score=eval_score.get("clarity"),
        completeness_score=eval_score.get("completeness"),
        maintainability_score=eval_score.get("maintainability"),
        overall_score=eval_score.get("overall_score"),
    )

    db.add(workflow)
    await db.commit()
    await db.refresh(workflow)

    return workflow