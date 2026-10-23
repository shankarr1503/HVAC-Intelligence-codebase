"""Script for training the energy consumption predictor on sample data."""
from src.models.energy_consumption_predictor import EnergyConsumptionPredictor
from src.data_pipeline.data_loader import DATASETS_DIR, load_csv
from src.data_pipeline.data_cleaning import drop_invalid_rows
from src.data_pipeline.feature_engineering import add_time_features


def main():
    # load dataset
    df = load_csv(str(DATASETS_DIR / 'sample_building_dataset.csv'))
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
