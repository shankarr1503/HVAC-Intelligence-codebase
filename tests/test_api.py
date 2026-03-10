"""Simple tests for FastAPI endpoints using TestClient."""
from fastapi.testclient import TestClient
from src.api.api_server import app

client = TestClient(app)

def test_predict_temperature_endpoint():
    resp = client.post("/predict-temperature", json={"features": {"a": 1, "b": 3}})
    assert resp.status_code == 200
    data = resp.json()
    assert "predicted" in data and isinstance(data["predicted"], float)


def test_comfort_score_endpoint():
    resp = client.post("/comfort-score", json={"temperature": 20, "humidity": 0.5})
    assert resp.status_code == 200
    data = resp.json()
    assert "comfort_score" in data
    assert 0.0 <= data["comfort_score"] <= 1.0


def test_optimize_hvac_endpoint():
    resp = client.post("/optimize-hvac", json={"current_temp": 19, "outside_temp": 10, "setpoint": 22})
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("action") in ["heat", "cool", "off"]
    assert isinstance(data.get("power"), (int, float))
