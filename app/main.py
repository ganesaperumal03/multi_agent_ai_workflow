from fastapi import FastAPI, Request
from app.api.routes import router
from app.utils.logger import generate_trace_id
from app.database.db_session import engine, Base

import contextvars

# ======================================
# Context Variable for Trace ID
# ======================================

trace_id_var = contextvars.ContextVar("trace_id", default="")

# ======================================
# Create FastAPI App
# ======================================

app = FastAPI(title="Multi-Agent AI Workflow")

# ======================================
# Middleware for Trace ID
# ======================================

@app.middleware("http")
async def add_trace_id(request: Request, call_next):
    trace_id = generate_trace_id()
    trace_id_var.set(trace_id)

    response = await call_next(request)
    response.headers["X-Trace-ID"] = trace_id
    return response


# ======================================
# Database Initialization (Startup Event)
# ======================================

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# ======================================
# Include API Routes
# ======================================

app.include_router(router)