from pydantic import BaseModel, Field
from typing import Dict


class TemperatureRequest(BaseModel):
    features: Dict[str, float] = Field(..., min_length=1)


class TemperatureResponse(BaseModel):
    predicted: float


class ComfortRequest(BaseModel):
    temperature: float
    humidity: float = Field(..., ge=0.0, le=1.0, description="Relative humidity as a fraction (0-1)")


class ComfortResponse(BaseModel):
    comfort_score: float


class OptimizeRequest(BaseModel):
    current_temp: float
    outside_temp: float
    setpoint: float


class OptimizeResponse(BaseModel):
    action: str
    power: float
