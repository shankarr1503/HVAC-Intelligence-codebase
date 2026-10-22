"""Reinforcement learning controller that interacts with an environment."""

from typing import Any, Tuple
import numpy as np


class RLController:
    """Reinforcement learning controller interface.

    The state vector is expected to contain the following elements in order:
    1. indoor_temperature (float)
    2. outdoor_temperature (float)
    3. humidity (float)
    4. occupancy (int)
    5. energy_consumption (float)

    Actions are represented as a tuple:
    (hvac_power_level, fan_speed, cooling_setpoint)
    where each component is typically normalized between 0 and 1 or -1 and 1.

    A reward function should balance energy usage and comfort;
    for example: `reward = -alpha*energy - beta*comfort_penalty`.
    """

    def __init__(self, policy=None):
        self.policy = policy

    def select_action(self, state: np.ndarray) -> Tuple[float, float, float]:
        """Return an action tuple for the given state."""
        if self.policy is None:
            # random exploration
            return (np.random.rand(), np.random.rand(), np.random.rand())
        return self.policy(state)

    def compute_reward(self, state: np.ndarray, action: Tuple[float, float, float]) -> float:
        """Example reward calculation. Override in subclasses or supply externally."""
        indoor_temp = state[0]
        energy = state[4]
        comfort_penalty = abs(indoor_temp - 22.0) / 10.0
        return -0.5 * energy - 0.5 * comfort_penalty

    def update_policy(self, experiences: Any) -> None:
        """Placeholder for policy update logic (e.g. PPO/DQN training step)."""
        pass
