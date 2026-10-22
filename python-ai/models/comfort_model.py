# comfort_model.py
"""Simple regression or classifier for comfort."""

import torch.nn as nn


class ComfortModel(nn.Module):
    def __init__(self, input_dim: int = 5, hidden_dim: int = 32, output_dim: int = 1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x)
