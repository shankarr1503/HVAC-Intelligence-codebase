# Energy Optimization Strategies

Energy optimization combines model predictions, control actions, and cost
functions to reduce electricity consumption while maintaining occupant comfort.

## Cost Function

The repository includes a basic `comfort_energy_cost` function (`src/optimization/cost_function.py`)
that computes a weighted sum of discomfort (1 - comfort score) and energy use.
The weighting parameter `alpha` can be tuned for different priorities.

## Optimizer

`energy_optimizer.minimize_energy` is a placeholder for more sophisticated
solvers. In research projects, this could wrap casadi solvers, genetic algorithms,
or custom gradient-based methods.

## Integration

Controllers can call the optimizer with predicted states and cost functions to
derive optimal setpoints or control sequences. For example, an MPC controller
would simulate future trajectories and evaluate the cost for each candidate
sequence.

> ⚠️ This module is intentionally lightweight; researchers are encouraged to
> plug in domain‑specific optimization algorithms and incorporate constraints
> (e.g., maximum power, comfort bounds, equipment wear).
