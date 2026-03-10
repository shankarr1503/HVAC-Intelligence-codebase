"""Demo script that calls the API prediction endpoints locally."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests


def main():
    url = "http://localhost:8000"
    data = {"features": {"temp": 20, "humidity": 0.5}}
    r = requests.post(f"{url}/predict-temperature", json=data)
    print("Temperature prediction:", r.json())

    data2 = {"temperature": 21.0, "humidity": 0.4}
    r2 = requests.post(f"{url}/comfort-score", json=data2)
    print("Comfort score:", r2.json())

    data3 = {"current_temp": 20.0, "outside_temp": 10.0, "setpoint": 22.0}
    r3 = requests.post(f"{url}/optimize-hvac", json=data3)
    print("Optimization result:", r3.json())


if __name__ == "__main__":
    main()
