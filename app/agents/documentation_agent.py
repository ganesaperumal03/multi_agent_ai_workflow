from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Running Documentation Agent", extra={"trace_id": "system"})


class DocumentationAgent(BaseAgent):
    def __init__(self):
        super().__init__("DocumentationAgent")

    async def run(self, input_data: dict) -> dict:
        refactored_code = input_data.get("refactored_code")

        prompt = f"""
        Generate professional documentation for the following code:

        {refactored_code}

        Include:
        - Overview
        - Installation
        - Usage
        - API reference
        - Example usage
        """

        response = await call_llm(prompt)

        return {"documentation": response}