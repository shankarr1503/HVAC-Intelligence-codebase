"""More detailed thermal dynamics used by building environment."""

from typing import Dict


class ThermalDynamicsModel:
    """Simulate heat transfer in a simple building envelope."""

    def __init__(self, capacitance: float = 500.0, resistance: float = 0.1):
        self.capacitance = capacitance  # thermal mass
        self.resistance = resistance   # insulation quality

    def step(self, indoor_temp: float, outdoor_temp: float, hvac_power: float, dt: float = 1.0) -> float:
        """Return new indoor temperature after dt hours."""
        # Newton's law of cooling with HVAC influence
        dT_out = (outdoor_temp - indoor_temp) / (self.resistance * self.capacitance)
        dT_hvac = hvac_power / self.capacitance
        return indoor_temp + (dT_out + dT_hvac) * dt
