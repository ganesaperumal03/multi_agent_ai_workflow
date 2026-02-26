from app.evaluation.agent_scorer import AgentScorer
from app.evaluation.output_validator import (
    OutputValidator,
    CodeOutputSchema,
    ReviewOutputSchema,
    RefactorOutputSchema,
    DocumentationOutputSchema
)
from app.agents.agent_registry import get_all_agents


import asyncio
from app.agents.agent_registry import get_all_agents
from app.memory.redis_memory import RedisMemory

class WorkflowService:

    def __init__(self):
        self.agents = get_all_agents()
        self.memory = RedisMemory()
        self.scorer = AgentScorer()

    async def execute_parallel(self, topic: str):

        research = await self.agents["research"].run({"topic": topic})
        code = await self.agents["code"].run(research)

        code_validated = OutputValidator.validate(CodeOutputSchema, code)

        review_task = self.agents["review"].run(code_validated)
        refactor_task = self.agents["refactor"].run(code_validated)

        review, refactor = await asyncio.gather(
            review_task,
            refactor_task,
            return_exceptions=True
        )

        review_validated = OutputValidator.validate(ReviewOutputSchema, review)
        refactor_validated = OutputValidator.validate(RefactorOutputSchema, refactor)

        documentation = await self.agents["documentation"].run(refactor_validated)
        documentation_validated = OutputValidator.validate(
            DocumentationOutputSchema,
            documentation
        )

        # Score final output
        score = await self.scorer.score_output(
            documentation_validated.get("documentation", ""),
            "Technical documentation quality"
        )

        final_output = {
            "research": research,
            "code": code_validated,
            "review": review_validated,
            "refactor": refactor_validated,
            "documentation": documentation_validated,
            "evaluation_score": score
        }

        await self.memory.save_session(topic, final_output)

        return final_output