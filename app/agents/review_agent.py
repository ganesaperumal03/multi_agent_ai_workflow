from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Running Review Agent", extra={"trace_id": "system"})


class ReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewAgent")

    async def run(self, input_data: dict) -> dict:
        code = input_data.get("generated_code")

        prompt = f"""
        Review the following Python code:

        {code}

        Provide:
        - Code quality assessment
        - Security concerns
        - Performance issues
        - Improvement suggestions
        """

        response = await call_llm(prompt)

        return {"review_feedback": response}