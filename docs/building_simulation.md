# Building Simulation

Simulation components model the thermal behavior of a building and the HVAC
system.

* `BuildingEnvironment` provides a wrapper with simple inertia-based temperature
  updates (see `src/simulation/building_environment.py`).
* `ThermalDynamicsModel` implements first-order thermal dynamics with
  resistance and capacitance parameters.
* `hvac_simulator.py` orchestrates running a controller against an environment.

Example usage scripts (`examples/simulate_building.py`,
`examples/realtime_optimization_demo.py`) demonstrate how to step through the
environment and compute costs.
