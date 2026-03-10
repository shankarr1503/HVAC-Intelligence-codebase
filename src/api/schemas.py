from pydantic import BaseModel
from typing import Dict


class TemperatureRequest(BaseModel):
    features: Dict[str, float]


class TemperatureResponse(BaseModel):
    predicted: float


class ComfortRequest(BaseModel):
    temperature: float
    humidity: float


class ComfortResponse(BaseModel):
    comfort_score: float


class OptimizeRequest(BaseModel):
    current_temp: float
    outside_temp: float
    setpoint: float


class OptimizeResponse(BaseModel):
    action: str
    power: float
