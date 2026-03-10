# Reinforcement Learning for HVAC Control

This document outlines the RL approach used in the platform.

- **State space:** indoor_temp, outdoor_temp, humidity, occupancy, energy_use
- **Action space:** continuous HVAC power level, optionally fan speed and setpoint
- **Reward:** negative weighted sum of energy consumption and comfort penalty
  (e.g. `-0.5*energy - 0.5*|temp-22|/10`).

The `RLController` class in `src/controllers` defines interfaces for selecting
actions and computing rewards. A simple custom gym environment is provided in
`src/training/train_rl_controller.py` for experimentation using stable-baselines3.

Researchers may replace the toy environment with a high‑fidelity simulator or
real data stream and plug in advanced RL algorithms.
