# passenger_data.py
"""Ingest passenger comfort preferences and biometric data."""

from typing import Dict, Any


def load_preferences(user_id: str) -> Dict[str, Any]:
    # Placeholder: fetch from database or static mapping
    return {"preferred_temp": 22.0, "sensitivity": 1.0}


def simulate_passenger() -> Dict[str, float]:
    return {"heart_rate": 70, "skin_temp": 33.0, "comfort_score": 0.8}
