from fastapi import FastAPI, Request
from app.api.routes import router
from app.utils.logger import generate_trace_id
import contextvars

trace_id_var = contextvars.ContextVar("trace_id", default="")

app = FastAPI(title="Multi-Agent AI Workflow")

@app.middleware("http")
async def add_trace_id(request: Request, call_next):
    trace_id = generate_trace_id()
    trace_id_var.set(trace_id)

    response = await call_next(request)
    response.headers["X-Trace-ID"] = trace_id
    return response

app.include_router(router)