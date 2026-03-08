# vehicle_energy_model.py
"""Estimate energy consumption from HVAC usage."""

def energy_usage(hvac_power: float, duration: float) -> float:
    # simple linear model
    return hvac_power * duration
