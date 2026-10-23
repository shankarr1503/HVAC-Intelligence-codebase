# HVAC Intelligence Codebase

> **Layout:** `src/` is the building-level research package (models, controllers,
> simulation and the `building-api` FastAPI service). `python-ai/` is the cabin
> climate AI service that the .NET backend (`dotnet-backend/`) calls. See
> `python-ai/README.md` for that service.


**Project Overview**

HVAC Intelligence is an open-source research platform for intelligent heating, ventilation,
and air-conditioning (HVAC) systems. It combines machine learning, reinforcement learning,
and optimization techniques to predict thermal comfort, minimize energy consumption, and
control building climate dynamically. The codebase is intended for engineers, researchers,
and contributors working on energy-efficient smart buildings.

**Problem Statement**

Traditional HVAC systems rely on simple thermostats and conservative setpoints, leading to
poor occupant comfort and excessive energy usage. Modern buildings generate vast amounts of
sensor data that can be harnessed by AI algorithms to anticipate thermal needs and adjust
HVAC operations proactively. HVAC Intelligence aims to provide a modular, extensible
toolkit that:

* Predicts occupant comfort and future temperatures
* Estimates energy consumption of HVAC units
* Optimizes control decisions using reinforcement learning and model predictive control
* Simulates building thermal dynamics for testing and validation

**Architecture Diagram & Description**

The system is organized into several components: data pipeline, machine learning models,
control algorithms, optimization routines, building simulation, and a FastAPI
service. An `architecture.md` document in the `docs/` directory provides a detailed
visual overview and explanation. Additional documentation covers the ML pipeline,
reinforcement learning methods, simulation mechanics and API endpoints.

See `docs/ml_pipeline.md`, `docs/reinforcement_learning.md`,
`docs/building_simulation.md`, and `docs/api_reference.md` for full details.

**Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/HVAC-Intelligence-codebase.git
   cd HVAC-Intelligence-codebase
   ```
2. Create and activate a Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # on macOS/Linux
   venv\Scripts\activate        # on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or install the package in editable mode for development
   pip install -e .
   ```
4. (Optional) run the full stack with Docker Compose:
   ```bash
   docker compose up --build
   ```
   | Service | Source | URL |
   |---|---|---|
   | `ai-service` | `python-ai/` | http://localhost:8000 |
   | `building-api` | `src/api` | http://localhost:8001 |
   | `backend` | `dotnet-backend/` | http://localhost:5000 |
   | `dashboard` | `dashboard/` | http://localhost:3000 |

**Example Usage**

* Train a model or run a simplified pipeline:
  ```bash
  python examples/train_model.py
  # or
  python examples/run_pipeline.py
  ```
* Train all models at once:
  ```bash
  python examples/train_models.py
  ```
* Simulate a building environment:
  ```bash
  python examples/simulate_building.py
  ```
* Demo real‑time optimization:
  ```bash
  python examples/realtime_optimization_demo.py
  ```
* Run a building simulation with an HVAC controller:
  ```bash
  python examples/run_simulation.py
  ```
* Demonstrate API predictions (requires server running):
  ```bash
  python examples/demo_prediction.py
  ```
* Start the API server for manual testing or integration:
  ```bash
  uvicorn src.api.api_server:app --reload
  ```

**Contribution Guide**

Please read `CONTRIBUTING.md` (or refer to `docs/` for instructions) before submitting
issues or pull requests. We welcome enhancements, bug fixes, new models, and improved
documentation. Follow these guidelines:

1. Fork the repository and create a feature branch.
2. Write clear, modular code and include tests.
3. Update documentation in `docs/` and add examples as needed.
4. Submit a pull request with a descriptive title and summary.

Refer to `CODE_OF_CONDUCT.md` for community standards.

**License**

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for
details.
