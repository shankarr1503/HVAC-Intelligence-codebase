# config.py
"""Configuration management using pydantic."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ai_service_port: int = 8000
    model_path: str = "./models"
    log_level: str = "INFO"
    # ... other configuration options


settings = Settings()
