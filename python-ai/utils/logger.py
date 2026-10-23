# logger.py
"""Simple logging configuration."""

import logging
from .config import settings


def get_logger(name: str) -> logging.Logger:
    handlers = [logging.StreamHandler()]
    if settings.log_file:
        handlers.append(logging.FileHandler(settings.log_file))
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        handlers=handlers,
    )
    return logging.getLogger(name)
