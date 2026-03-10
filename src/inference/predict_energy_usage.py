"""Utility to load a trained energy model and perform predictions."""
import numpy as np


def predict(model, features: np.ndarray) -> np.ndarray:
    """Return predicted energy usage."""
    return model.predict(features)


if __name__ == '__main__':
    # example usage
    from src.models.energy_consumption_predictor import EnergyConsumptionPredictor
    model = EnergyConsumptionPredictor()
    # assume model has been fitted elsewhere
    X = np.random.rand(5, 2)
    print(predict(model, X))
