"""Simple HVAC simulation harness using the building environment and controllers."""

from typing import Dict
from .building_environment import BuildingEnvironment


def run_simulation(controller, steps: int = 24) -> Dict[int, float]:
    env = BuildingEnvironment()
    temps = {}
    for t in range(steps):
        state = {
            "temperature": env.current_temp
        }
        action = controller.compute(state['temperature']) if hasattr(controller, 'compute') else controller.select_action(state)
        power = action.get('power', 0) if isinstance(action, dict) else action
        temps[t] = env.step(power)
    return temps
