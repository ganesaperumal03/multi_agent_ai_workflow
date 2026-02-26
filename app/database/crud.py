from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import WorkflowRun


async def create_workflow_run(
    db: AsyncSession,
    topic: str,
    result: dict,
):
    workflow = WorkflowRun(
        topic=topic,
        research=result.get("research", {}).get("research"),
        generated_code=result.get("code", {}).get("generated_code"),
        review_feedback=result.get("review", {}).get("review_feedback"),
        refactored_code=result.get("refactor", {}).get("refactored_code"),
        documentation=result.get("documentation", {}).get("documentation"),
        quality_score=result["evaluation_score"].get("quality"),
        clarity_score=result["evaluation_score"].get("clarity"),
        completeness_score=result["evaluation_score"].get("completeness"),
        maintainability_score=result["evaluation_score"].get("maintainability"),
        overall_score=result["evaluation_score"].get("overall_score"),
    )

    db.add(workflow)
    await db.commit()
    await db.refresh(workflow)

    return workflow