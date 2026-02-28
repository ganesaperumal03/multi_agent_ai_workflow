import json
from app.utils.llm_provider import call_llm
import re

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

        Do NOT include markdown.
        Do NOT include explanations.
        Do NOT include extra text.

        Output to evaluate:
        {output}
        """

        response = await call_llm(prompt)

        #  Extract JSON block safely
        try:
            json_match = re.search(r"\{.*\}", response, re.DOTALL)
            if not json_match:
                raise ValueError("No JSON found")

            clean_json = json_match.group(0)
            return json.loads(clean_json)

        except Exception:
            return {
                "quality": 0,
                "clarity": 0,
                "completeness": 0,
                "maintainability": 0,
                "overall_score": 0,
                "error": "Invalid JSON from evaluator"
            }