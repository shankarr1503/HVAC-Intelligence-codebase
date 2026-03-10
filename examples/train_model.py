"""Example script showing model training workflow."""
import sys, os
# ensure root directory is on the path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.models.thermal_comfort_model import ThermalComfortModel


def main():
    # synthetic dataset
    X = np.random.rand(100, 3)
    y = np.random.rand(100)

    model = ThermalComfortModel()
    model.train(X, y)
    preds = model.predict(X[:5])
    print("Training complete, sample predictions:", preds)


if __name__ == "__main__":
    main()
