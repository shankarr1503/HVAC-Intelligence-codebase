"""FastAPI server providing prediction and optimization endpoints."""

from fastapi import FastAPI
from .routes import router

app = FastAPI(title="HVAC Intelligence API")
app.include_router(router)
