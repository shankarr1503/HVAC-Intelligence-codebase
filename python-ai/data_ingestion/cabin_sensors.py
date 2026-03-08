# cabin_sensors.py
"""Module for ingesting cabin sensor data."""

import json
from typing import Dict, Any


def read_sensors(filepath: str) -> Dict[str, Any]:
    """Read cabin sensor data from a file (JSON for simulation)."""
    with open(filepath, "r") as f:
        return json.load(f)


def simulate_sensors() -> Dict[str, float]:
    """Generate synthetic sensor data for simulation mode."""
    # Placeholder: return fixed values or random
    return {
        "cabin_temp": 22.0,
        "humidity": 40.0,
        "outside_temp": 15.0,
        "sunlight": 0.2,
        "vehicle_speed": 0.0,
        "passenger_count": 1,
        "battery_state": 0.8,
        "hvac_power": 0.0,
        "seat_temp": 22.0,
        "heart_rate": 70,
        "skin_temp": 33.0,
        "air_quality": 0.9,
    }
