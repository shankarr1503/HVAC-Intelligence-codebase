"""Separate routing logic for the FastAPI app."""
from fastapi import APIRouter
from .schemas import (
    TemperatureRequest,
    TemperatureResponse,
    ComfortRequest,
    ComfortResponse,
    OptimizeRequest,
    OptimizeResponse,
)

router = APIRouter()


@router.post("/predict-temperature", response_model=TemperatureResponse)
async def predict_temperature(req: TemperatureRequest):
    predicted = sum(req.features.values()) / len(req.features)
    return TemperatureResponse(predicted=predicted)


@router.post("/comfort-score", response_model=ComfortResponse)
async def comfort_score(req: ComfortRequest):
    score = max(0.0, 1 - abs(req.temperature - 22) / 10)
    return ComfortResponse(comfort_score=score)


@router.post("/optimize-hvac", response_model=OptimizeResponse)
async def optimize_hvac(req: OptimizeRequest):
    # power is signed like BuildingEnvironment.step: positive heats, negative cools
    action = "off"
    power = 0.0
    if req.current_temp < req.setpoint - 0.5:
        action = "heat"
        power = 1.0
    elif req.current_temp > req.setpoint + 0.5:
        action = "cool"
        power = -1.0
    return OptimizeResponse(action=action, power=power)
