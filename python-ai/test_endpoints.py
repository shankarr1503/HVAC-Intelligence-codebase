import requests
import json

base_url = "http://localhost:8000"

def test_endpoint(path, data=None, method="POST"):
    url = f"{base_url}{path}"
    print(f"Testing {method} {url}...")
    try:
        if method == "POST":
            resp = requests.post(url, json=data)
        else:
            resp = requests.get(url)
        print(f"Status: {resp.status_code}")
        print(f"Response: {json.dumps(resp.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

print("--- HEALH CHECK ---")
test_endpoint("/health", method="GET")

print("\n--- PREDICT TEMPERATURE ---")
predict_data = {
    "cabin_temp": 22,
    "outside_temp": 20,
    "humidity": 50,
    "solar_radiation": 0.1,
    "vehicle_speed": 0,
    "passenger_count": 1,
    "battery_level": 0.8,
    "hvac_power": 0,
    "skin_temperature": 33,
    "heart_rate": 70,
    "seat_temperature": 22,
    "air_quality": 0.9
}
test_endpoint("/predict-temperature", predict_data)

print("\n--- COMFORT SCORE ---")
comfort_data = {"temp": 22, "humidity": 50, "heart_rate": 70, "skin_temp": 33, "seat_temp": 22}
test_endpoint("/comfort-score", comfort_data)

print("\n--- OPTIMIZE HVAC ---")
optimize_data = {"current_temp": 22, "target_temp": 21}
test_endpoint("/optimize-hvac", optimize_data)
