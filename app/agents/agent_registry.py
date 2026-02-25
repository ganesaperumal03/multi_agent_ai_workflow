from app.agents.research_agent import ResearchAgent
from app.agents.code_generator_agent import CodeGeneratorAgent
from app.agents.review_agent import ReviewAgent
from app.agents.refactor_agent import RefactorAgent
from app.agents.documentation_agent import DocumentationAgent

def get_all_agents():
    return {
        "research": ResearchAgent(),
        "code": CodeGeneratorAgent(),
        "review": ReviewAgent(),
        "refactor": RefactorAgent(),
        "documentation": DocumentationAgent(),
    }