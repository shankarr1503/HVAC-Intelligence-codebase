import pytest
import numpy as np

try:
    from models.temperature_predictor import TemperaturePredictor
    from models.comfort_model import ComfortModel
    import torch
except ImportError:
    TemperaturePredictor = None
    ComfortModel = None
    torch = None


def test_temp_predictor_forward():
    if TemperaturePredictor is None or torch is None:
        pytest.skip("torch not installed; skipping temp predictor test")
    model = TemperaturePredictor()
    x = np.zeros((1, 12), dtype=np.float32)
    y = model(torch.from_numpy(x))
    assert y.shape == (1, 1)


def test_comfort_model_forward():
    if ComfortModel is None or torch is None:
        pytest.skip("torch not installed; skipping comfort model test")
    model = ComfortModel()
    x = np.zeros((1, 5), dtype=np.float32)
    y = model(torch.from_numpy(x))
    assert y.shape == (1, 1)
