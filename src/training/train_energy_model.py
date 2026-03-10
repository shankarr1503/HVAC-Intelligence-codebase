"""Script for training the energy consumption predictor on sample data."""
import numpy as np
from pathlib import Path
from src.models.energy_consumption_predictor import EnergyConsumptionPredictor
from src.data_pipeline.data_loader import load_csv
from src.data_pipeline.data_cleaning import drop_invalid_rows
from src.data_pipeline.feature_engineering import add_time_features


def main():
    # load dataset
    df = load_csv('datasets/sample_building_dataset.csv')
    df = drop_invalid_rows(df, ['temperature', 'humidity', 'energy_use'])
    df = add_time_features(df)
    X = df[['temperature', 'humidity']].values
    y = df['energy_use'].values

    model = EnergyConsumptionPredictor()
    model.fit(X, y)
    print('Energy model trained, coefficients:', model.model)
    # save model or return


if __name__ == '__main__':
    main()
