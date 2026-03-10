"""Functions for computing comfort-related penalties."""


def temperature_penalty(temp: float, setpoint: float = 22.0) -> float:
    """Calculate penalty based on deviation from a setpoint."""
    return abs(temp - setpoint) / 10.0
