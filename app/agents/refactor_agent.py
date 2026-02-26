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
        if not code:
            raise ValueError("code is required")

        prompt = f"""
        You are a senior Python code reviewer.

        Refactor the following Python code to improve:

        - Readability
        - Performance
        - Maintainability
        - Error handling
        - Compliance with PEP8

        Original Code:
        {code}

        Requirements:
        - Preserve original functionality.
        - Improve variable naming if necessary.
        - Add type hints.
        - Add docstrings.
        - Optimize inefficient logic.
        - Remove redundant code.

        Output Rules:
        - Return only the refactored Python code.
        - Do not include explanations.
        """

        try:
            response = await call_llm(prompt)
        except Exception as e:
            logger.error("LLM call failed", exc_info=True)
            raise

        return {"refactored_code": response}