"""Pseudo real-time optimization demonstration."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from src.controllers.rule_based_controller import RuleBasedController
from src.optimization.cost_function import comfort_energy_cost
from src.simulation.building_environment import BuildingEnvironment


def main():
    env = BuildingEnvironment()
    controller = RuleBasedController(setpoint=22)

    for t in range(24):
        state_temp = env.current_temp
        action = controller.compute(state_temp)
        cost = comfort_energy_cost(1 - abs(state_temp - 22)/10, abs(action['power']))
        print(f"t={t}: temp={state_temp:.2f}, action={action}, cost={cost:.3f}")
        env.step(action['power'])
        time.sleep(0.1)


if __name__ == '__main__':
    main()
