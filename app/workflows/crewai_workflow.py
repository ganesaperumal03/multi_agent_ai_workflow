from crewai import Agent, Task, Crew, Process, LLM
from app.config import settings
import asyncio
from app.evaluation.agent_scorer import AgentScorer


async def run_crewai(topic: str):


    llm = LLM(
        model=f"groq/{settings.GROQ_MODEL}",
        temperature=0.1,
        api_key=settings.GROQ_API_KEY,
    )

    research_agent = Agent(
        role="Research Specialist",
        goal="Conduct deep research",
        backstory="Expert technical analyst",
        verbose=True,
        llm=llm
    )

    code_agent = Agent(
        role="Senior Python Developer",
        goal="Generate clean code",
        backstory="Production-level backend engineer",
        verbose=True,
        llm=llm
    )

    review_agent = Agent(
        role="Code Reviewer",
        goal="Review code quality",
        backstory="Security and performance expert",
        verbose=True,
        llm=llm
    )

    research_task = Task(
        description=f"Research in detail about {topic}",
        agent=research_agent,
        expected_output="Structured research findings"
    )

    code_task = Task(
        description="Generate production-level Python code using research findings.",
        agent=code_agent,
        context=[research_task],
        expected_output="Clean, production-ready Python code with proper structure and documentation",
    )

    review_task = Task(
        description="Review the generated code and provide structured feedback.",
        agent=review_agent,
        context=[code_task],
        expected_output="Detailed code review with suggestions for improvements, security issues, and best practices",
    )

    crew = Crew(
        agents=[research_agent, code_agent, review_agent],
        tasks=[research_task, code_task, review_task],
        process=Process.sequential
    )

    result = await asyncio.to_thread(crew.kickoff)

    scorer = AgentScorer()

    score = await scorer.score_output(
        str(result),
        "Technical documentation quality"
    )

    return {
        "crewai_output": result,
        "evaluation_score": score
    }

