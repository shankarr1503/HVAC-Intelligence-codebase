"""Example script to train multiple models at once."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.models.thermal_comfort_model import ThermalComfortModel
from src.models.energy_consumption_predictor import EnergyConsumptionPredictor
from src.models.occupancy_prediction_model import OccupancyPredictionModel


def main():
    # generate synthetic dataset
    X = np.random.rand(100, 3)
    y_temp = np.random.rand(100)
    y_energy = np.random.rand(100)
    y_occ = (np.random.rand(100) > 0.5).astype(int)

    tm = ThermalComfortModel()
    tm.train(X, y_temp)
    print("Trained thermal comfort model")

    em = EnergyConsumptionPredictor()
    em.fit(X[:, :2], y_energy)
    print("Trained energy predictor")

    om = OccupancyPredictionModel()
    om.train(X, y_occ)
    print("Trained occupancy model")


if __name__ == '__main__':
    main()
