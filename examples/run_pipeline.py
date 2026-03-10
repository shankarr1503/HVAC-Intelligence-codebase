"""Demo of a complete ML pipeline: load, preprocess, train, evaluate."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_pipeline.data_loader import load_sample_data
from src.data_pipeline.preprocessing import clean_data, normalize
from src.data_pipeline.feature_engineering import add_time_features
from src.models.thermal_comfort_model import ThermalComfortModel


def main():
    df = load_sample_data()
    df = clean_data(df)
    df = add_time_features(df)
    # assume temperature predicts energy use as comfort proxy
    X = df[['temperature', 'humidity']].values
    y = df['energy_use'].values

    model = ThermalComfortModel()
    model.train(X, y)
    preds = model.predict(X)
    print('Model trained on sample data, predictions:', preds)


if __name__ == '__main__':
    main()
