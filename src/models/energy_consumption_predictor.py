"""Predictor for HVAC energy consumption."""

from typing import Any
import numpy as np


class EnergyConsumptionPredictor:
    def __init__(self):
        self.model = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """Train a simple regression model"""
        # simple linear regression using normal equations
        self.model = np.linalg.pinv(X.T @ X) @ X.T @ y

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise ValueError("Model not trained")
        return X @ self.model
