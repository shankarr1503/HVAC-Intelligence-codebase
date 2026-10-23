"""Tests for the optimizer, MPC controller and data loaders."""
import numpy as np

from src.controllers.mpc_controller import MPCController
from src.optimization.energy_optimizer import minimize_energy


def test_minimize_energy_finds_minimum():
    x = minimize_energy(lambda v: float((v[0] - 3.0) ** 2), [0.0])
    assert abs(x[0] - 3.0) < 1e-3


def test_minimize_energy_respects_bounds():
    x = minimize_energy(lambda v: float((v[0] - 3.0) ** 2), [0.0], bounds=[(-1.0, 1.0)])
    assert abs(x[0] - 1.0) < 1e-6


def test_mpc_heats_when_cold_and_cools_when_hot():
    mpc = MPCController(horizon=5)
    assert mpc.compute_control(np.array([15.0, 10.0]))[0] > 0
    assert mpc.compute_control(np.array([28.0, 30.0]))[0] < 0


def test_sample_datasets_load_from_any_cwd(tmp_path, monkeypatch):
    from src.data_pipeline.data_loader import DATASETS_DIR, load_csv, load_sample_data
    monkeypatch.chdir(tmp_path)
    assert 'energy_use' in load_sample_data().columns
    df = load_csv(str(DATASETS_DIR / 'sample_building_dataset.csv'))
    assert list(df.columns)[0] == 'timestamp'
