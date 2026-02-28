from app.config import settings
from app.workflows.langgraph_workflow import run_langgraph
from app.workflows.crewai_workflow import run_crewai
from app.services.workflow_service import WorkflowService

service = WorkflowService()

async def run_workflow(topic: str):
    if settings.WORKFLOW_ENGINE == "langgraph":
        return await run_langgraph(topic)
    elif settings.WORKFLOW_ENGINE == "crewai":
        return await run_crewai(topic)
    elif settings.WORKFLOW_ENGINE == "orchestrator":
        service = WorkflowService()
        return await service.execute_parallel(topic)

    else:
        raise ValueError("Invalid workflow engine")