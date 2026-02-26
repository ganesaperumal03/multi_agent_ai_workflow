from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db
from app.database.crud import create_workflow_run
from fastapi import APIRouter
from app.api.schemas import WorkflowRequest
from app.services.workflow_service import WorkflowService

router = APIRouter()
service = WorkflowService()

@router.post("/execute")
async def execute_workflow(
    request: WorkflowRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await service.execute_parallel(request.topic)

    await create_workflow_run(db, request.topic, result)

    return result