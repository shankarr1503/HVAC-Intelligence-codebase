# temperature_predictor.py
"""Deep network for cabin temperature forecasting."""

import torch
import torch.nn as nn


class TemperaturePredictor(nn.Module):
    def __init__(self, input_dim: int = 12, hidden_dim: int = 64, output_dim: int = 1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)


def predict(model: TemperaturePredictor, features):
    model.eval()
    with torch.no_grad():
        return model(features)
