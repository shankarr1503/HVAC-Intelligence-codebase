"""State estimator that maintains HVAC system state over time."""

from typing import Dict, Any


class HVACStateEstimator:
    def __init__(self):
        self.state: Dict[str, Any] = {}

    def update(self, measurements: Dict[str, Any]) -> None:
        """Update internal state with new measurements."""
        self.state.update(measurements)

    def get_state(self) -> Dict[str, Any]:
        """Return current estimated state."""
        return self.state.copy()
