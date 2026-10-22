# API Reference

The FastAPI service exposes the following endpoints:

* `POST /predict-temperature` – accepts JSON with `features` map and returns
  `{predicted: float}`.
* `POST /comfort-score` – accepts `temperature` and `humidity`, returns
  `{comfort_score: float}` between 0 and 1.
* `POST /optimize-hvac` – accepts `current_temp`, `outside_temp`, `setpoint`,
  returns `{action: str, power: float}` from a simple rule-based policy.
  `power` is signed: positive heats, negative cools.

Schemas are defined in `src/api/schemas.py` and routing logic in
`src/api/routes.py`. OpenAPI documentation is automatically served at
`/docs` when the server is running.
