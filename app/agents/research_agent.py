from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Running Research Agent", extra={"trace_id": "system"})


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent")

    async def run(self, input_data: dict) -> dict:
        topic = input_data.get("topic")

        prompt = f"""
        You are an expert technical researcher.
        Conduct detailed research on: {topic}

        Provide:
        - Key concepts
        - Important techniques
        - Best practices
        - Challenges
        - Real-world applications
        """

        response = await call_llm(prompt)

        return {"research": response}