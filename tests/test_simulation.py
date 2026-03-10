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
