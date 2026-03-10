"""Preprocessing routines such as normalization and missing value handling."""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: drop NA and reset index."""
    return df.dropna().reset_index(drop=True)


def normalize(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Min-max normalize the given columns."""
    result = df.copy()
    for col in columns:
        minv = result[col].min()
        maxv = result[col].max()
        if maxv > minv:
            result[col] = (result[col] - minv) / (maxv - minv)
    return result
