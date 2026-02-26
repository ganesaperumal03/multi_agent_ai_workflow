from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm

from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Running Code Generator Agent")


class CodeGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("CodeGeneratorAgent")

    async def run(self, input_data: dict) -> dict:
        research_content = input_data.get("research")
        if not research_content:
            raise ValueError("Research content is required")

        prompt = f"""
        You are a senior Python software engineer.

        Based on the research below, generate production-ready Python code.

        Research:
        {research_content}

        Requirements:
        - Follow SOLID principles
        - Use modular design
        - Use type hints
        - Include docstrings
        - Add proper error handling
        - Follow PEP8 guidelines

        Output Rules:
        - Only return valid Python code.
        - Do NOT include explanations.
        - Do NOT include markdown.
        - Code must be executable.
        """

        try:
            response = await call_llm(prompt)
        except Exception as e:
            logger.error("LLM call failed", exc_info=True)
            raise

        return {"generated_code": response}