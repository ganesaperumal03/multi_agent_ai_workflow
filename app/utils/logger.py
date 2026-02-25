import logging
import uuid


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s | trace_id=%(trace_id)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def generate_trace_id():
    return str(uuid.uuid4())