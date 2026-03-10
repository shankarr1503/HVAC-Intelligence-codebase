"""Data loading utilities for building sensor datasets."""

from typing import List
import pandas as pd


def load_csv(filepath: str) -> pd.DataFrame:
    """Load dataset from a CSV file (handles BOM).

    Parameters
    ----------
    filepath : str
        Path to the CSV file. Relative paths are resolved against the current
        working directory.
    """
    return pd.read_csv(filepath, encoding='utf-8-sig')


def load_sample_data() -> pd.DataFrame:
    """Return a small sample dataset included with the repo."""
    return load_csv('datasets/sample_building_data.csv')
