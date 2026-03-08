# ai_service_api.py
"""FastAPI server exposing prediction and optimization endpoints for CLI integration with C# backend."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
import numpy as np
import torch

from models.temperature_predictor import TemperaturePredictor, predict as temp_predict
from models.comfort_model import ComfortModel
from control.mpc_controller import MPCController
from feature_engineering.comfort_index import compute_comfort_score
from utils.logger import get_logger
from utils.config import settings

logger = get_logger(__name__)

app = FastAPI(title="AI Climate Control Service")

# Pydantic request/response models
class SensorData(BaseModel):
    cabin_temp: float
    outside_temp: float
    humidity: float
    solar_radiation: float
    vehicle_speed: float
    passenger_count: int
    battery_level: float
    hvac_power: float
    skin_temperature: float
    heart_rate: float
    seat_temperature: float
    air_quality: float

class PredictionResponse(BaseModel):
    predicted_temp: float

class ComfortRequest(BaseModel):
    temp: float
    humidity: float
    heart_rate: float
    skin_temp: float
    seat_temp: float

class ComfortResponse(BaseModel):
    comfort_score: float

class OptimizationRequest(BaseModel):
    current_temp: float
    target_temp: float

class OptimizationResponse(BaseModel):
    hvac_setting: float

# load models (placeholder: assume saved models)
TEMP_MODEL = TemperaturePredictor()
COMFORT_MODEL = ComfortModel()
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
        pred = temp_predict(TEMP_MODEL, torch.from_numpy(features).float())
        return PredictionResponse(predicted_temp=float(pred.flatten()[0]))
    except Exception as e:
        import traceback
        logger.error(f"Error in prediction: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/comfort-score", response_model=ComfortResponse)
def comfort_score(req: ComfortRequest):
    try:
        # first try ML model, fallback to engineered index
        features = np.array([[req.temp, req.humidity, req.heart_rate, req.skin_temp, req.seat_temp]], dtype=np.float32)
        score = COMFORT_MODEL(torch.from_numpy(features).float())
        val = float(score.detach().numpy().flatten()[0])
        if val == 0.0:
            val = compute_comfort_score(req.temp, req.humidity, req.heart_rate, req.skin_temp, req.seat_temp)
        return ComfortResponse(comfort_score=val)
    except Exception as e:
        import traceback
        logger.error(f"Error in comfort score: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize-hvac", response_model=OptimizationResponse)
def optimize_hvac(req: OptimizationRequest):
    try:
        setting = MPC.solve(req.current_temp, req.target_temp, outside_temp=req.current_temp)  # assume outside equals current for simplicity
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
