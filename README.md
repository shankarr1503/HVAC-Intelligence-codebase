# Intelligent Predictive Climate Control System

This repository contains a research-grade platform for optimizing passenger comfort and energy efficiency in electric/autonomous vehicles using AI, reinforcement learning, and model predictive control.

## Architecture

- **python-ai** – machine learning, prediction, ML pipelines, simulation, AI service REST API.
- **dotnet-backend** – vehicle communication, HVAC control logic, REST controllers, streaming service.
- **dashboard** – React front-end for real-time monitoring.
- **docker-compose.yml** – orchestrates services for local development.

## Requirements

- Python 3.11
- .NET 8 SDK
- Docker & Docker Compose
- Node.js (for dashboard)

## Getting Started

### Python AI Service

```bash
cd python-ai
python -m venv venv
source venv/Scripts/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python main_ai_service.py
``` 

### .NET Backend

Navigate to `dotnet-backend` and restore/build:  
```bash
cd dotnet-backend
dotnet restore
dotnet run
```

### Dashboard

```bash
cd dashboard
npm install
npm start
```

### Using Docker Compose

```bash
docker-compose up --build
```

### Simulation Mode

The Python simulator generates synthetic data and posts to the backend. Run:
```bash
python python-ai/simulation/simulator.py
```

* The simulator can also be extended to emit CAN bus messages via the C# `CanBusInterface.SimulateTelemetry` helper, enabling full digital‑twin testing of the vehicle layer.


## Training

Temperature model:
```
python python-ai/training/train_temperature_model.py
```

RL agent and environment:
```
python python-ai/training/train_rl_model.py
```

The `ClimateEnv` environment now contains simple thermal dynamics and a reward function rewarding comfort while penalizing energy use.  It terminates when battery depletes.  A unit test (`python-ai/tests/test_env_mpc.py`) verifies both the environment and the MPC solver.

## API Endpoints

- `POST /predict-temperature` – returns predicted cabin temperature.
- `POST /comfort-score` – returns passenger comfort score.
- `POST /optimize-hvac` – returns optimal HVAC setting.
- `POST /api/sensor/data` – ingest sensor data (C# backend).

## Project Structure

See description above or inspect directories.

## Testing

Unit tests for Python modules are located under `python-ai/tests`. Run them with pytest from the `python-ai` directory:

```bash
pytest tests
```

The .NET backend can add MSTest/NUnit projects later; current code is stubbed.

## API Documentation

FastAPI automatically provides OpenAPI/Swagger at `http://localhost:8000/docs` when the AI service is running.

The .NET backend has Swagger UI at `http://localhost:5000/swagger` once started in development mode, documenting the climate and sensor endpoints.

## Example Dataset

Located at `python-ai/data_ingestion/example_dataset.csv`.

---

Further development should expand models, add unit/integration tests, implement real CAN bus interfaces, and flesh out the React dashboard with charts and WebSocket connectivity.
