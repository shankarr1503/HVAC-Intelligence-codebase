"""Run comfort model inference."""
import numpy as np


def predict(model, features: np.ndarray) -> np.ndarray:
    return model.predict(features)


if __name__ == '__main__':
    from src.models.thermal_comfort_model import ThermalComfortModel
    model = ThermalComfortModel()
    X = np.random.rand(3, 3)
    print("Sample comfort predictions", predict(model, X))
