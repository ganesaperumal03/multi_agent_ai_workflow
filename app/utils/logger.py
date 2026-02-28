import logging
import uuid
from contextvars import ContextVar

# Create global trace context
trace_id_var = ContextVar("trace_id", default="system")


class TraceIdFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = trace_id_var.get()
        return True


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s | trace_id=%(trace_id)s"
        )

        handler.setFormatter(formatter)

        handler.addFilter(TraceIdFilter())

        logger.addHandler(handler)

    return logger


def generate_trace_id():
    return str(uuid.uuid4())