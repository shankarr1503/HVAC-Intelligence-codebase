from fastapi.testclient import TestClient
from services.ai_service_api import app

client = TestClient(app)


def test_predict_temperature():
    payload = {
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
    resp = client.post("/predict-temperature", json=payload)
    assert resp.status_code == 200
    assert "predicted_temp" in resp.json()


def test_comfort_score():
    payload = {"temp":22, "humidity":50, "heart_rate":70, "skin_temp":33, "seat_temp":22}
    resp = client.post("/comfort-score", json=payload)
    assert resp.status_code == 200
    score = resp.json().get("comfort_score", -1)
    assert 0 <= score <= 1
    # check engineered fallback
    assert score >= 0.0

# if torch is not installed the prediction model will return default or error

if __name__ == "__main__":
    print("Testing predict_temperature...")
    test_predict_temperature()
    print("Testing comfort_score...")
    test_comfort_score()
    print("All tests passed!")
