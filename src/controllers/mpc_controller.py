"""Model predictive controller (MPC) for the building environment."""

import numpy as np

from src.optimization.energy_optimizer import minimize_energy


class MPCController:
    """Plan HVAC power over a horizon using the ``BuildingEnvironment`` dynamics.

    Each step the indoor temperature relaxes towards the outside temperature by
    ``leak_rate`` and HVAC power (-1 cools, +1 heats) adds ``power_gain`` degrees.
    """

    def __init__(self, horizon: int = 10, setpoint: float = 22.0, energy_weight: float = 0.1,
                 leak_rate: float = 0.1, power_gain: float = 0.5):
        self.horizon = horizon
        self.setpoint = setpoint
        self.energy_weight = energy_weight
        self.leak_rate = leak_rate
        self.power_gain = power_gain

    def _cost(self, powers: np.ndarray, indoor: float, outdoor: float) -> float:
        cost = 0.0
        temp = indoor
        for p in powers:
            temp += (outdoor - temp) * self.leak_rate + p * self.power_gain
            cost += (temp - self.setpoint) ** 2 + self.energy_weight * p ** 2
        return cost

    def compute_control(self, current_state: np.ndarray) -> np.ndarray:
        """Return the planned power sequence for state ``[indoor_temp, outdoor_temp, ...]``.

        Apply the first element and re-plan at the next step.
        """
        indoor, outdoor = float(current_state[0]), float(current_state[1])
        return minimize_energy(lambda u: self._cost(u, indoor, outdoor),
                               np.zeros(self.horizon), bounds=[(-1.0, 1.0)] * self.horizon)

    def compute(self, temperature: float, outside_temp: float = 15.0) -> dict:
        """Rule-controller-compatible interface used by ``run_simulation``."""
        power = float(self.compute_control(np.array([temperature, outside_temp]))[0])
        return {"mode": "heating" if power > 0 else "cooling" if power < 0 else "off", "power": power}
