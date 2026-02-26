from crewai import Agent, Task, Crew, Process
from app.utils.llm_provider import call_llm
import asyncio


async def run_crewai(topic: str):

    research_agent = Agent(
        role="Research Specialist",
        goal="Conduct deep research",
        backstory="Expert technical analyst",
        verbose=True,
    )

    code_agent = Agent(
        role="Senior Python Developer",
        goal="Generate clean code",
        backstory="Production-level backend engineer",
        verbose=True,
    )

    review_agent = Agent(
        role="Code Reviewer",
        goal="Review code quality",
        backstory="Security and performance expert",
        verbose=True,
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
    )

    review_task = Task(
        description="Review the generated code and provide structured feedback.",
        agent=review_agent,
        context=[code_task],
    )

    crew = Crew(
        agents=[research_agent, code_agent, review_agent],
        tasks=[research_task, code_task, review_task],
        process=Process.sequential
    )

    result = await asyncio.to_thread(crew.kickoff)

    return {"crewai_output": result}