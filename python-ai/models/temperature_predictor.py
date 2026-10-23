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
        # input normalization statistics, saved with the weights in state_dict
        self.register_buffer("feature_mean", torch.zeros(input_dim))
        self.register_buffer("feature_std", torch.ones(input_dim))

    def set_normalization(self, features: torch.Tensor):
        self.feature_mean.copy_(features.mean(dim=0))
        self.feature_std.copy_(features.std(dim=0) + 1e-6)

    def forward(self, x):
        return self.net((x - self.feature_mean) / self.feature_std)


def predict(model: TemperaturePredictor, features):
    model.eval()
    with torch.no_grad():
        return model(features)
