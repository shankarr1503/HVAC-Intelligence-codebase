# thermal_features.py
"""Feature engineering functions for thermal data."""

import numpy as np


def compute_heat_load(inside_temp: float, outside_temp: float, sunlight: float) -> float:
    """Simplistic heat load estimate."""
    return (outside_temp - inside_temp) * 0.5 + sunlight * 10


def estimate_metabolism(heart_rate: float, skin_temp: float) -> float:
    """Estimate passenger metabolic heat generation."""
    # placeholder linear model
    return 0.1 * heart_rate + 0.05 * skin_temp


def compute_solar_gain(area: float, solar_radiation: float) -> float:
    """Compute solar heat gain through windows."""
    return area * solar_radiation * 0.7


def normalize_features(features: np.ndarray) -> np.ndarray:
    return (features - np.mean(features, axis=0)) / (np.std(features, axis=0) + 1e-6)
