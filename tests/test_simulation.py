"""Tests for simulation components."""
from src.simulation.building_environment import BuildingEnvironment
from src.simulation.thermal_dynamics_model import ThermalDynamicsModel


def test_building_environment_step():
    env = BuildingEnvironment()
    initial = env.current_temp
    new_temp = env.step(0.5)
    assert new_temp != initial


def test_thermal_dynamics_model():
    dyn = ThermalDynamicsModel()
    temp = dyn.step(20.0, 10.0, 0.5)
    assert isinstance(temp, float)


def test_rule_based_cooling_lowers_temperature():
    from src.controllers.rule_based_controller import RuleBasedController
    env = BuildingEnvironment(outside_temp=30.0)
    controller = RuleBasedController(setpoint=22.0)
    for _ in range(20):
        env.step(controller.compute(env.current_temp)['power'])
    assert env.current_temp < 26.0


def test_simulation_runs_with_rl_controller():
    from src.controllers.reinforcement_learning_controller import RLController
    from src.simulation.hvac_simulator import run_simulation
    temps = run_simulation(RLController(), steps=3)
    assert len(temps) == 3
