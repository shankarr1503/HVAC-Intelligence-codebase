# logger.py
"""Simple logging configuration."""

import logging
from .config import settings


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=getattr(logging, settings.log_level),
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(name)
