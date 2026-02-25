import json
from app.utils.llm_provider import call_llm


class AgentScorer:

    async def score_output(self, output: str, criteria: str) -> dict:
        prompt = f"""
        You are an AI evaluation system.

        Evaluate the following output based on:
        {criteria}

        Provide score (1-10) for:
        - Quality
        - Clarity
        - Completeness
        - Maintainability

        Return ONLY valid JSON in this format:

        {{
            "quality": int,
            "clarity": int,
            "completeness": int,
            "maintainability": int,
            "overall_score": float
        }}

        Output to evaluate:
        {output}
        """

        response = await call_llm(prompt)

        try:
            return json.loads(response)
        except Exception:
            return {
                "quality": 0,
                "clarity": 0,
                "completeness": 0,
                "maintainability": 0,
                "overall_score": 0,
                "error": "Invalid JSON from evaluator"
            }