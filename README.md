# Multi-Agent AI Workflow Automation System

An AI-first engineering platform that orchestrates multiple intelligent agents to automate research, code generation, review, refactoring, and documentation — built with production-grade architecture.

---

## Project Overview

This project demonstrates how to design and implement a scalable, production-ready multi-agent AI system with:

- Parallel agent execution
- LLM-based evaluation scoring
- JSON schema output validation
- Memory persistence with Redis
- Workflow orchestration using LangGraph, CrewAI, and a custom Orchestrator
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

The system supports **three** workflow engines, selectable via the `WORKFLOW_ENGINE` environment variable:

| Engine         | Value          | Description                                                  |
| -------------- | -------------- | ------------------------------------------------------------ |
| LangGraph      | `langgraph`    | Graph-based orchestration with state management              |
| CrewAI         | `crewai`       | Role-based multi-agent framework with sequential processing  |
| Orchestrator   | `orchestrator` | Custom async service with parallel agent execution           |

```env
# Choose your workflow engine
WORKFLOW_ENGINE=langgraph
# or
WORKFLOW_ENGINE=crewai
# or
WORKFLOW_ENGINE=orchestrator
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
- Groq LLM (Meta LLaMA 4 Scout)

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
│
├── app/
│   ├── main.py                  # FastAPI app entry point + middleware
│   ├── config.py                # Pydantic settings (env-based config)
│   ├── dependencies.py          # Dependency injection (DB session)
│   │
│   ├── api/
│   │   ├── routes.py            # API endpoints (/execute)
│   │   └── schemas.py           # Request/response Pydantic models
│   │
│   ├── agents/
│   │   ├── base_agent.py        # Abstract base agent class
│   │   ├── research_agent.py    # Research specialist agent
│   │   ├── code_generator_agent.py  # Code generation agent
│   │   ├── review_agent.py      # Code review agent
│   │   ├── refactor_agent.py    # Code refactoring agent
│   │   ├── documentation_agent.py   # Documentation agent
│   │   └── agent_registry.py   # Agent factory/registry
│   │
│   ├── database/
│   │   ├── db_session.py        # Async SQLAlchemy engine + session
│   │   ├── models.py            # WorkflowRun ORM model
│   │   └── crud.py              # Database CRUD operations
│   │
│   ├── workflows/
│   │   ├── workflow_selector.py # Engine router (langgraph/crewai/orchestrator)
│   │   ├── langgraph_workflow.py    # LangGraph-based workflow
│   │   ├── crewai_workflow.py       # CrewAI-based workflow
│   │   └── state_manager.py    # Workflow state TypedDict
│   │
│   ├── memory/
│   │   └── redis_memory.py      # Redis-based session memory
│   │
│   ├── evaluation/
│   │   ├── agent_scorer.py      # LLM-based output scoring
│   │   └── output_validator.py  # JSON schema validation
│   │
│   ├── services/
│   │   └── workflow_service.py  # Orchestrator workflow service
│   │
│   └── utils/
│       ├── llm_provider.py      # LLM API abstraction layer
│       └── logger.py            # Structured logging setup
│
├── Dockerfile                   # Container image definition
├── docker-compose.yml           # Multi-service orchestration
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
└── README.md
```

Clean separation of:

- Agent logic
- Workflow orchestration
- Memory layer
- Evaluation layer
- API layer
- Infrastructure configuration

---

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# ==============================
# LLM Configuration (Required)
# ==============================
GROQ_API_KEY=your_groq_api_key_here
LLM_PROVIDER=groq
GROQ_MODEL=meta-llama/llama-4-scout-17b-16e-instruct

# ==============================
# Workflow Engine (Required)
# ==============================
# Options: langgraph | crewai | orchestrator
WORKFLOW_ENGINE=orchestrator

# ==============================
# Database (Required)
# ==============================
DATABASE_URL=postgresql://user:password@postgres:5432/db

# ==============================
# Redis (Required)
# ==============================
REDIS_URL=redis://redis:6379
```

| Variable          | Description                                      | Required | Default         |
| ----------------- | ------------------------------------------------ | -------- | --------------- |
| `GROQ_API_KEY`    | API key for Groq LLM provider                   | Yes      | —               |
| `LLM_PROVIDER`    | LLM backend to use                               | No       | `groq`          |
| `GROQ_MODEL`      | Model identifier for Groq                        | No       | `meta-llama/llama-4-scout-17b-16e-instruct` |
| `WORKFLOW_ENGINE` | Workflow engine: `langgraph`, `crewai`, or `orchestrator` | No | `orchestrator` |
| `DATABASE_URL`    | PostgreSQL connection string                     | No       | `postgresql://user:password@localhost/db` |
| `REDIS_URL`       | Redis connection string                          | No       | `redis://localhost:6379` |

> **Note:** When running with Docker Compose, use `postgres` and `redis` as hostnames (service names) instead of `localhost`.

---

## Docker Setup

### Dockerfile

The application uses a multi-stage production-ready Dockerfile:

- **Base image:** `python:3.11-slim`
- **System deps:** `build-essential`, `curl`
- **App server:** Uvicorn on port `8000`
- Bytecode generation disabled (`PYTHONDONTWRITEBYTECODE=1`)
- Unbuffered output for real-time logging (`PYTHONUNBUFFERED=1`)

### Docker Compose Services

The `docker-compose.yml` defines three services:

| Service    | Image              | Port   | Description                    |
| ---------- | ------------------ | ------ | ------------------------------ |
| `api`      | Built from `./`    | `8000` | FastAPI application server     |
| `redis`    | `redis:7`          | —      | In-memory store for agent memory |
| `postgres` | `postgres:15`      | `5432` | Persistent database for workflow runs |

Access the API docs at: **http://localhost:8000/docs**

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

## Author

**Ganesaperumal S**
AI/ML Engineer | GenAI Systems Developer
Specialized in multi-agent architectures, RAG pipelines, and AI workflow engineering.

---

## License

MIT License