# train_temperature_model.py
"""Script to train temperature prediction model."""

import torch
from models.temperature_predictor import TemperaturePredictor


def main():
    # placeholder training loop
    model = TemperaturePredictor()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(10):
        # simulate data
        x = torch.randn(32, 12)
        y = torch.randn(32, 1)
        pred = model(x)
        loss = torch.nn.functional.mse_loss(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch}, loss {loss.item()}")


if __name__ == "__main__":
    main()
