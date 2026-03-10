"""Model predictive controller (MPC) stub implementation."""

from typing import Any
import numpy as np


class MPCController:
    def __init__(self, horizon: int = 10):
        self.horizon = horizon

    def compute_control(self, current_state: np.ndarray) -> Any:
        """Compute control action over planning horizon."""
        # stub: return zeros
        return np.zeros_like(current_state)
