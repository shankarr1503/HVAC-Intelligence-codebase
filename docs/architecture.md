# System Architecture

The HVAC Intelligence platform is divided into modular components:

* **Data Pipeline** – responsible for ingestion of sensor data, cleaning, and
  feature engineering. Files live under `src/data_pipeline/`.
* **Models** – predictive models estimating thermal comfort, energy consumption,
  and HVAC state. Stored in `src/models/`.
* **Controllers** – decision-making algorithms including reinforcement learning,
  model predictive control (MPC) and rule-based heuristics. Located in
  `src/controllers/`.
* **Optimization** – utility routines for cost calculation and energy optimization
  strategies (`src/optimization/`).
* **Simulation** – environment and simulator for testing controllers in a
  simplified building thermal model (`src/simulation/`).
* **API** – FastAPI server exposing prediction and control endpoints
  (`src/api/api_server.py`).

A high-level architecture diagram (`diagrams/system_architecture.png`) illustrates
component interactions. Data flows from sensors into the pipeline, models generate
predictions, controllers use these in decision-making, and the API allows external
clients to query and command the system.
