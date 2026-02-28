from app.agents.base_agent import BaseAgent
from app.utils.llm_provider import call_llm
from app.utils.logger import get_logger

logger = get_logger(__name__)



class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent")

    async def run(self, input_data: dict) -> dict:
        logger.info("Running Research Agent")

        topic = input_data.get("topic")
        if not topic:
            raise ValueError("topic  is required")

        prompt = f"""
        You are a senior technical research analyst.

        Conduct in-depth research on the topic below.

        Topic:
        {topic}

        Instructions:
        - Be precise and structured.
        - Use clear headings.
        - Use bullet points where appropriate.
        - Avoid vague explanations.

        Output Format (strictly follow this structure):

        ## Overview
        Brief introduction to the topic.

        ## Key Concepts
        - Concept 1
        - Concept 2
        - Concept 3

        ## Important Techniques
        - Technique 1
        - Technique 2

        ## Best Practices
        - Practice 1
        - Practice 2

        ## Challenges
        - Challenge 1
        - Challenge 2

        ## Real-World Applications
        - Application 1
        - Application 2
        """
        try:
            response = await call_llm(prompt)
        except Exception as e:
            logger.error("LLM call failed", exc_info=True)
            raise

        return {"research": response}