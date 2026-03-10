"""Thermal comfort prediction using simple regression or neural network."""

from typing import Any
import numpy as np


class ThermalComfortModel:
    def __init__(self):
        # placeholder for trained parameters
        self.coefficients = None

    def train(self, X: np.ndarray, y: np.ndarray):
        """Train a simple linear model"""
        # using least squares for illustration
        self.coefficients = np.linalg.pinv(X) @ y

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict comfort score given feature matrix"""
        if self.coefficients is None:
            raise ValueError("Model has not been trained")
        return X @ self.coefficients
