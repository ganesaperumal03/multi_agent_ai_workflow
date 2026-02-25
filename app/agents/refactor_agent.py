from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Running Refactor Agent", extra={"trace_id": "system"})


class RefactorAgent(BaseAgent):
    def __init__(self):
        super().__init__("RefactorAgent")

    async def run(self, input_data: dict) -> dict:
        code = input_data.get("generated_code")

        prompt = f"""
        Refactor the following Python code to:

        - Improve readability
        - Improve performance
        - Follow PEP8
        - Add error handling

        Code:
        {code}
        """

        response = await call_llm(prompt)

        return {"refactored_code": response}