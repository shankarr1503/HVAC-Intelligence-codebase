# config.py
"""Configuration management using pydantic."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ai_service_port: int = 8000
    model_path: str = "./artifacts"  # trained weights, separate from the models/ package
    log_file: str = ""  # empty disables file logging
    log_level: str = "INFO"
    reload: bool = False  # uvicorn auto-reload, for local development only
    # ... other configuration options


settings = Settings()
