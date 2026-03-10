"""Data cleaning utilities for HVAC datasets."""

import pandas as pd
from typing import List


def drop_invalid_rows(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Drop rows where any of the specified columns contain NaN or invalid values."""
    clean = df.copy()
    clean = clean.dropna(subset=columns)
    return clean


def convert_types(df: pd.DataFrame, dtype_map: dict) -> pd.DataFrame:
    """Ensure columns have specified data types."""
    return df.astype(dtype_map)
