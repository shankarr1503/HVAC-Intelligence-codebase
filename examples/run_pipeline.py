"""Demo of a complete ML pipeline: load, preprocess, train, evaluate."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_pipeline.data_loader import load_sample_data
from src.data_pipeline.preprocessing import clean_data
from src.data_pipeline.feature_engineering import add_time_features
from src.models.energy_consumption_predictor import EnergyConsumptionPredictor


def main():
    df = load_sample_data()
    df = clean_data(df)
    df = add_time_features(df)
    # predict HVAC energy use from indoor/outdoor conditions
    X = df[['temperature', 'humidity', 'outside_temp']].values
    y = df['energy_use'].values

    model = EnergyConsumptionPredictor()
    model.fit(X, y)
    preds = model.predict(X)
    print('Model trained on sample data, predictions:', preds)


if __name__ == '__main__':
    main()
