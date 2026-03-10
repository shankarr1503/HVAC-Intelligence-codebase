"""Run a simple building simulation with a rule-based controller."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.rule_based_controller import RuleBasedController
from src.simulation.hvac_simulator import run_simulation


def main():
    controller = RuleBasedController(setpoint=22.0)
    temps = run_simulation(controller, steps=48)
    print("Simulated temperatures:")
    for t, temp in temps.items():
        print(f"hour {t}: {temp:.2f} C")


if __name__ == "__main__":
    main()
