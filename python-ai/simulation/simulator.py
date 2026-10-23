# simulator.py
"""Standalone simulation engine for generating synthetic sensor and telemetry data."""

import os
import random
import time
import requests

# backend sensor ingestion endpoint; use http://backend:8080/sensor-data inside docker compose
API_URL = os.environ.get("BACKEND_SENSOR_URL", "http://localhost:5000/sensor-data")


def generate_data():
    return {
        "CabinTemp": random.uniform(18, 26),
        "OutsideTemp": random.uniform(-5, 35),
        "Humidity": random.uniform(20, 80),
        "SolarRadiation": random.uniform(0, 1),
        "VehicleSpeed": random.uniform(0, 120),
        "PassengerCount": random.randint(1,4),
        "BatteryLevel": random.uniform(0.2, 1.0),
        "HvacPower": random.uniform(0,1),
        "SkinTemperature": random.uniform(30, 36),
        "HeartRate": random.uniform(60, 100),
        "SeatTemperature": random.uniform(20, 30),
        "AirQuality": random.uniform(0.5, 1.0)
    }


def run_simulation(interval=1.0):
    while True:
        data = generate_data()
        try:
            requests.post(API_URL, json=data, timeout=5).raise_for_status()
        except Exception as e:
            print(f"failed to send: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    run_simulation()
