"""Feature engineering helpers for thermal models."""

import pandas as pd


def add_time_features(df: pd.DataFrame, timestamp_col: str = 'timestamp') -> pd.DataFrame:
    """Derive hour, dayofweek and period-of-day from a timestamp column."""
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    df['hour'] = df[timestamp_col].dt.hour
    df['dayofweek'] = df[timestamp_col].dt.dayofweek
    # categorize into morning/afternoon/evening/night
    df['period'] = pd.cut(df['hour'], bins=[-1,5,11,17,23], labels=['night','morning','afternoon','evening'])
    return df


def add_occupancy_features(df: pd.DataFrame, occupancy_col: str = 'occupancy') -> pd.DataFrame:
    """Create binary and rolling features from occupancy counts."""
    df = df.copy()
    df['occupied'] = df[occupancy_col] > 0
    df['occupancy_rolling_mean'] = df[occupancy_col].rolling(window=3, min_periods=1).mean()
    return df
