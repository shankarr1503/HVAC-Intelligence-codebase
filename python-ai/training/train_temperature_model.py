# train_temperature_model.py
"""Script to train temperature prediction model on simulator data."""

import csv
import tempfile
from pathlib import Path

import torch
from models.temperature_predictor import TemperaturePredictor
from training.generate_synthetic_data import create_dataset
from utils.config import settings


def load_dataset(n: int = 5000):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "synthetic_data.csv"
        create_dataset(str(path), n)
        with open(path, newline="") as f:
            rows = [[float(v) for v in row] for row in list(csv.reader(f))[1:]]
    data = torch.tensor(rows, dtype=torch.float32)
    return data[:, :12], data[:, 12:]


def main(epochs: int = 1000, val_fraction: float = 0.2):
    x, y = load_dataset()
    n_val = int(len(x) * val_fraction)
    x_train, y_train, x_val, y_val = x[n_val:], y[n_val:], x[:n_val], y[:n_val]

    model = TemperaturePredictor()
    model.set_normalization(x_train)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)
    for epoch in range(epochs):
        model.train()
        loss = torch.nn.functional.mse_loss(model(x_train), y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, loss {loss.item()}")

    model.eval()
    with torch.no_grad():
        val_loss = torch.nn.functional.mse_loss(model(x_val), y_val).item()
    print(f"Validation MSE {val_loss:.4f}")

    out_dir = Path(settings.model_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), out_dir / "temperature_predictor.pt")
    print(f"Saved weights to {out_dir / 'temperature_predictor.pt'}")


if __name__ == "__main__":
    main()
