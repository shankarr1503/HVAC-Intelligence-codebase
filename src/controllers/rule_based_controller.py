"""Simple rule-based HVAC controller."""

from typing import Dict, Any


class RuleBasedController:
    def __init__(self, setpoint: float = 22.0):
        self.setpoint = setpoint

    def compute(self, temperature: float) -> Dict[str, Any]:
        """Decide HVAC mode based on temperature relative to setpoint.

        ``power`` is signed to match ``BuildingEnvironment.step``:
        positive heats, negative cools.
        """
        if temperature < self.setpoint - 1:
            return {"mode": "heating", "power": 1.0}
        elif temperature > self.setpoint + 1:
            return {"mode": "cooling", "power": -1.0}
        else:
            return {"mode": "off", "power": 0.0}
