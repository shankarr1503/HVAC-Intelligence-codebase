"""Unit tests for core model classes."""
import numpy as np
from src.models.thermal_comfort_model import ThermalComfortModel
from src.models.energy_consumption_predictor import EnergyConsumptionPredictor


def test_thermal_comfort_model():
    X = np.random.rand(10, 3)
    y = np.random.rand(10)
    m = ThermalComfortModel()
    m.train(X, y)
    preds = m.predict(X)
    assert preds.shape == (10,)


def test_energy_consumption_predictor():
    X = np.random.rand(10, 2)
    y = np.random.rand(10)
    e = EnergyConsumptionPredictor()
    e.fit(X, y)
    p = e.predict(X)
    assert p.shape == (10,)


def test_occupancy_prediction_model():
    from src.models.occupancy_prediction_model import OccupancyPredictionModel
    X = np.random.rand(10, 2)
    y = (np.random.rand(10) > 0.5).astype(int)
    m = OccupancyPredictionModel()
    m.train(X, y)
    preds = m.predict(X)
    assert preds.shape == (10,)


def test_rule_based_controller():
    from src.controllers.rule_based_controller import RuleBasedController
    c = RuleBasedController(setpoint=22)
    assert c.compute(20)['mode'] == 'heating'
    assert c.compute(24)['mode'] == 'cooling'
    assert c.compute(22)['mode'] == 'off'


def test_simulation_runs():
    from src.controllers.rule_based_controller import RuleBasedController
    from src.simulation.hvac_simulator import run_simulation
    temps = run_simulation(RuleBasedController(), steps=5)
    assert len(temps) == 5
