from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)



class ReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewAgent")

    async def run(self, input_data: dict) -> dict:
        logger.info("Running Review Agent")

        code = input_data.get("generated_code")
        if not code:
            raise ValueError("code is required")

        prompt = f"""
        You are a senior Python code auditor.

        Review the following code:

        {code}

        Provide structured feedback in this format:

        ## Code Quality Assessment
        - Clarity:
        - Maintainability:
        - Structure:

        ## Security Concerns
        - Issue 1:
        - Issue 2:

        ## Performance Issues
        - Issue 1:
        - Issue 2:

        ## Improvement Suggestions
        - Suggestion 1:
        - Suggestion 2:

        Be specific and actionable.
        """

        try:
            response = await call_llm(prompt)
        except Exception as e:
            logger.error("LLM call failed", exc_info=True)
            raise

        return {"review_feedback": response}