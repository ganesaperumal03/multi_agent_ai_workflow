from langgraph.graph import StateGraph
from app.workflows.state_manager import WorkflowState
from app.agents.agent_registry import get_all_agents
import asyncio


async def run_langgraph(topic: str):

    agents = get_all_agents()

    async def research_node(state: WorkflowState):
        result = await agents["research"].run({"topic": state["topic"]})
        state.update(result)
        return state

    async def code_node(state: WorkflowState):
        result = await agents["code"].run(state)
        state.update(result)
        return state

    async def parallel_node(state: WorkflowState):
        review_task = agents["review"].run(state)
        refactor_task = agents["refactor"].run(state)

        review, refactor = await asyncio.gather(review_task, refactor_task)

        state.update(review)
        state.update(refactor)
        return state

    async def documentation_node(state: WorkflowState):
        result = await agents["documentation"].run(state)
        state.update(result)
        return state

    builder = StateGraph(WorkflowState)

    builder.add_node("research", research_node)
    builder.add_node("code", code_node)
    builder.add_node("parallel", parallel_node)
    builder.add_node("documentation", documentation_node)

    builder.set_entry_point("research")
    builder.add_edge("research", "code")
    builder.add_edge("code", "parallel")
    builder.add_edge("parallel", "documentation")

    graph = builder.compile()

    initial_state = {"topic": topic}

    final_state = await graph.ainvoke(initial_state)

    return final_state