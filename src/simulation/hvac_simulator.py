"""Simple HVAC simulation harness using the building environment and controllers."""

from typing import Dict
import numpy as np
from .building_environment import BuildingEnvironment


def run_simulation(controller, steps: int = 24) -> Dict[int, float]:
    env = BuildingEnvironment()
    temps = {}
    for t in range(steps):
        if hasattr(controller, 'compute'):
            power = controller.compute(env.current_temp).get('power', 0.0)
        else:
            # RLController state layout: indoor, outdoor, humidity, occupancy, energy;
            # the first action component is the HVAC power level
            state = np.array([env.current_temp, env.outside_temp, 0.5, 0, 0.0])
            power = float(controller.select_action(state)[0])
        temps[t] = env.step(power)
    return temps
