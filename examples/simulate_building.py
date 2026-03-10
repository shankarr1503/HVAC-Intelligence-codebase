"""Example showing building simulation with thermal dynamics."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.simulation.building_environment import BuildingEnvironment
from src.simulation.thermal_dynamics_model import ThermalDynamicsModel


def main():
    env = BuildingEnvironment()
    dyn = ThermalDynamicsModel()
    indoor = env.current_temp
    for hour in range(24):
        action = 0.1  # constant small heating
        indoor = dyn.step(indoor, env.outside_temp, action)
        print(f"Hour {hour}: {indoor:.2f} C")


if __name__ == '__main__':
    main()
