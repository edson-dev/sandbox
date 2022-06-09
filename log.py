import logging
import os
from typing import Callable
import time
from functools import wraps


class Log:
    def __new__(self):
        format = "[%(levelname)s][%(asctime)s][%(funcName)s]-[line %(lineno)d]-> %(message)s "
        level = os.getenv("LOG_LEVEL") if os.getenv("LOG_LEVEL") else logging.INFO
        logging.basicConfig(encoding='utf-8', level=level, format=format)
        return logging


def timed(func: Callable) -> object:
    """Print the execution time for the decorated function.
    Args:
        func (Callable): Function to be logged.
    Returns:
        function: Return decorator.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(
            "{} ran in {}s".format(func.__name__, round(end - start, 2))
        )
        return result

    return wrapper
