from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm

from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Running Code Generator Agent", extra={"trace_id": "system"})


class CodeGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("CodeGeneratorAgent")

    async def run(self, input_data: dict) -> dict:
        research_content = input_data.get("research")

        prompt = f"""
        Based on the following research:

        {research_content}

        Generate clean, production-level Python code.
        Follow best practices and modular design.
        """

        response = await call_llm(prompt)

        return {"generated_code": response}