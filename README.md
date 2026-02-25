# Multi-Agent AI Workflow Automation System

An AI-first engineering platform that orchestrates multiple intelligent agents to automate research, code generation, review, refactoring, and documentation — built with production-grade architecture.

---

## Project Overview

This project demonstrates how to design and implement a scalable, production-ready multi-agent AI system with:

- Parallel agent execution
- LLM-based evaluation scoring
- JSON schema output validation
- Memory persistence with Redis
- Workflow orchestration using LangGraph and CrewAI
- FastAPI-based async backend
- PostgreSQL integration
- Dockerized deployment
- Observability with tracing and logging

**This is not a chatbot — it is an AI workflow orchestration engine.**

---

## System Architecture

```
User Request
     |
Research Agent
     |
Code Generator Agent
     |
Parallel Execution:
    -> Review Agent
    -> Refactor Agent
     |
Documentation Agent
     |
Validation + AI Scoring
     |
Persist to Redis + PostgreSQL
     |
Return Structured Response
```

---

## Agents

| Agent                  | Responsibility                                 |
| ---------------------- | ---------------------------------------------- |
| Research Agent         | Conducts structured topic research             |
| Code Generator Agent   | Produces production-grade Python code           |
| Review Agent           | Evaluates code quality and security            |
| Refactor Agent         | Optimizes and improves code                    |
| Documentation Agent    | Generates professional technical documentation |

Each agent operates independently and communicates via structured state objects.

---

## Workflow Engines

The system supports environment-based engine switching:

```env
WORKFLOW_ENGINE=langgraph
# or
WORKFLOW_ENGINE=crewai
```

This demonstrates:

- Modular orchestration layer
- Pluggable workflow engines
- Enterprise-ready configurability

---

## Tech Stack

### Backend

- Python 3.11+
- FastAPI (async)
- LangGraph
- CrewAI
- OpenAI API

### Infrastructure

- Redis — memory tracking
- PostgreSQL — persistence
- Docker and Docker Compose

### Engineering Features

- Async parallel execution
- JSON Schema validation (Pydantic)
- LLM-based output scoring
- Structured logging
- Trace ID middleware
- Environment-based configuration

---

## Project Structure

```
multi_agent_ai_workflow/
|
+-- app/
|   +-- main.py
|   +-- config.py
|   |
|   +-- api/
|   |   +-- routes.py
|   |   +-- schemas.py
|   |
|   +-- agents/
|   |   +-- base_agent.py
|   |   +-- research_agent.py
|   |   +-- code_generator_agent.py
|   |   +-- review_agent.py
|   |   +-- refactor_agent.py
|   |   +-- documentation_agent.py
|   |   +-- agent_registry.py
|   |
|   +-- workflows/
|   |   +-- workflow_selector.py
|   |   +-- langgraph_workflow.py
|   |   +-- crewai_workflow.py
|   |   +-- state_manager.py
|   |
|   +-- memory/
|   |   +-- redis_memory.py
|   |
|   +-- evaluation/
|   |   +-- agent_scorer.py
|   |   +-- output_validator.py
|   |
|   +-- services/
|   |   +-- workflow_service.py
|   |
|   +-- utils/
|       +-- llm_provider.py
|       +-- logger.py
|
+-- docker/
|   +-- Dockerfile
|   +-- docker-compose.yml
|
+-- requirements.txt
+-- .env
+-- README.md
```

Clean separation of:

- Agent logic
- Workflow orchestration
- Memory layer
- Evaluation layer
- API layer
- Infrastructure configuration

---

## Key Engineering Highlights

### Parallel Agent Execution

Uses `asyncio.gather` to execute Review and Refactor agents concurrently, reducing overall pipeline latency.

### AI-Based Evaluation System

The LLM evaluates output quality and generates structured scoring metrics across quality, clarity, completeness, and maintainability.

### JSON Output Validation

Strict Pydantic schema validation ensures reliability and structured outputs at every agent boundary.

### Observability

- Trace ID middleware for request tracking
- Structured logging across all agents
- Error handling hooks

### Memory Persistence

Redis session storage enables workflow tracking and state recall across requests.

---

## Example API Request

```http
POST /execute
Content-Type: application/json

{
  "topic": "Design a scalable FastAPI microservice"
}
```

---

## Sample Output Structure

```json
{
  "research": "...",
  "code": "...",
  "review": "...",
  "refactor": "...",
  "documentation": "...",
  "evaluation_score": {
    "quality": 8,
    "clarity": 9,
    "completeness": 8,
    "maintainability": 9,
    "overall_score": 8.5
  }
}
```

---

## Running with Docker

```bash
docker-compose up --build
```

Access the API docs at: http://localhost:8000/docs

---

## Why This Project Matters

This project demonstrates:

- Advanced multi-agent system design
- AI workflow orchestration at scale
- Production-ready backend engineering
- LLM output validation and scoring
- Clean architecture principles
- Enterprise AI system thinking

It reflects real-world AI platform engineering practices beyond simple chatbot implementations.

---

## Future Enhancements

- Prometheus metrics integration
- Agent retry and fault tolerance
- Performance benchmarking dashboard
- Vector database integration
- Multi-tenant support

---

## License

MIT License