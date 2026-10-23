# ai_service_api.py
"""FastAPI server exposing prediction and optimization endpoints for CLI integration with C# backend."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
import uvicorn
import numpy as np
import torch

from models.temperature_predictor import TemperaturePredictor, predict as temp_predict
from models.comfort_model import ComfortModel
from control.mpc_controller import MPCController
from feature_engineering.comfort_index import compute_comfort_score
from simulation.cabin_thermal_simulator import simulate_step
from utils.logger import get_logger
from utils.config import settings

logger = get_logger(__name__)

app = FastAPI(title="AI Climate Control Service")

# Pydantic request/response models; bounds reject physically implausible input
Temperature = Field(..., ge=-50, le=80, description="degrees C")
Percent = Field(..., ge=0, le=100)
Fraction = Field(..., ge=0, le=1)


class SensorData(BaseModel):
    cabin_temp: float = Temperature
    outside_temp: float = Temperature
    humidity: float = Percent
    solar_radiation: float = Fraction
    vehicle_speed: float = Field(..., ge=0, le=300, description="km/h")
    passenger_count: int = Field(..., ge=0, le=20)
    battery_level: float = Fraction
    hvac_power: float = Field(..., ge=-2, le=2)
    skin_temperature: float = Temperature
    heart_rate: float = Field(..., ge=0, le=250)
    seat_temperature: float = Temperature
    air_quality: float = Fraction

class PredictionResponse(BaseModel):
    predicted_temp: float

class ComfortRequest(BaseModel):
    temp: float = Temperature
    humidity: float = Percent
    heart_rate: float = Field(..., ge=0, le=250)
    skin_temp: float = Temperature
    seat_temp: float = Temperature

class ComfortResponse(BaseModel):
    comfort_score: float

class OptimizationRequest(BaseModel):
    current_temp: float = Temperature
    target_temp: float = Field(..., ge=10, le=35, description="degrees C")
    outside_temp: float = Field(20.0, ge=-50, le=80, description="degrees C")

class OptimizationResponse(BaseModel):
    hvac_setting: float

def _load_weights(model: torch.nn.Module, filename: str):
    """Return the model with trained weights, or None if no weights exist."""
    path = Path(settings.model_path) / filename
    if not path.exists():
        logger.warning(f"No trained weights at {path}; using fallback")
        return None
    model.load_state_dict(torch.load(path, map_location="cpu"))
    model.eval()
    return model


# trained models are optional; without weights the endpoints use the
# physics simulator and engineered comfort index instead of random networks
TEMP_MODEL = _load_weights(TemperaturePredictor(), "temperature_predictor.pt")
COMFORT_MODEL = _load_weights(ComfortModel(), "comfort_model.pt")
MPC = MPCController()

@app.post("/predict-temperature", response_model=PredictionResponse)
def predict_temperature(data: SensorData):
    try:
        features = np.array([[
            data.cabin_temp,
            data.outside_temp,
            data.humidity,
            data.solar_radiation,
            data.vehicle_speed,
            data.passenger_count,
            data.battery_level,
            data.hvac_power,
            data.skin_temperature,
            data.heart_rate,
            data.seat_temperature,
            data.air_quality,
        ]], dtype=np.float32)
        if TEMP_MODEL is None:
            pred = simulate_step(data.cabin_temp, data.outside_temp, data.hvac_power,
                                 data.solar_radiation, 0.1 * data.passenger_count)
            return PredictionResponse(predicted_temp=float(pred))
        pred = temp_predict(TEMP_MODEL, torch.from_numpy(features).float())
        return PredictionResponse(predicted_temp=float(pred.flatten()[0]))
    except Exception as e:
        import traceback
        logger.error(f"Error in prediction: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/comfort-score", response_model=ComfortResponse)
def comfort_score(req: ComfortRequest):
    try:
        # use the trained ML model when available, otherwise the engineered index
        if COMFORT_MODEL is None:
            val = compute_comfort_score(req.temp, req.humidity, req.heart_rate, req.skin_temp, req.seat_temp)
            return ComfortResponse(comfort_score=val)
        features = np.array([[req.temp, req.humidity, req.heart_rate, req.skin_temp, req.seat_temp]], dtype=np.float32)
        with torch.no_grad():
            score = COMFORT_MODEL(torch.from_numpy(features).float())
        return ComfortResponse(comfort_score=float(score.numpy().flatten()[0]))
    except Exception as e:
        import traceback
        logger.error(f"Error in comfort score: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize-hvac", response_model=OptimizationResponse)
def optimize_hvac(req: OptimizationRequest):
    try:
        setting = MPC.solve(req.current_temp, req.target_temp, outside_temp=req.outside_temp)
        return OptimizationResponse(hvac_setting=setting)
    except Exception as e:
        import traceback
        logger.error(f"Error in MPC: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

# additional endpoints for health checks, metrics, etc.
@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.ai_service_port)
