from fastapi import APIRouter
from app.api.schemas import WorkflowRequest
from app.services.workflow_service import WorkflowService

router = APIRouter()
service = WorkflowService()

@router.post("/execute")
async def execute_workflow(request: WorkflowRequest):
    result = await service.execute_parallel(request.topic)
    return result