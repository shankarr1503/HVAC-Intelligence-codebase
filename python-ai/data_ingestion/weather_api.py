# weather_api.py
"""Wrapper for external weather API calls."""

from typing import Dict, Any


def get_current_weather(location: str) -> Dict[str, Any]:
    # Placeholder implementation
    return {"temperature": 20.0, "humidity": 50.0, "sunlight": 0.5}
