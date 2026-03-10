"""Model to predict building occupancy from environmental data."""
from typing import Any, Optional
import numpy as np
from sklearn.linear_model import LogisticRegression


class OccupancyPredictionModel:
    def __init__(self):
        self.model: Optional[LogisticRegression] = None

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """Train a logistic regression classifier."""
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict(X)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict_proba(X)
