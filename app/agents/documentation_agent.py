from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)




class DocumentationAgent(BaseAgent):
    def __init__(self):
        super().__init__("DocumentationAgent")

    async def run(self, input_data: dict) -> dict:
        logger.info("Running Documentation Agent")
        refactored_code = input_data.get("refactored_code")
        if not refactored_code:
            raise ValueError("refactored_code content is required")

        prompt = f"""
        You are a technical documentation specialist.

        Generate professional documentation for the following Python code.

        Code:
        {refactored_code}

        Requirements:
        - Clear and concise language
        - Suitable for GitHub README
        - Structured with markdown headings

        Output Format:

        # Project Title

        ## Overview
        Brief description of the project.

        ## Installation
        Step-by-step installation instructions.

        ## Usage
        How to run and use the project.

        ## API Reference
        Explain important classes and functions.

        ## Example Usage
        Provide a working example.
        """

        try:
            response = await call_llm(prompt)
        except Exception as e:
            logger.error("LLM call failed", exc_info=True)
            raise

        return {"documentation": response}