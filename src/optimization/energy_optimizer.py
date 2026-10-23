"""Optimization routines for energy consumption."""

from typing import Callable, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import minimize


def minimize_energy(cost_function: Callable[[np.ndarray], float], initial_guess,
                    bounds: Optional[Sequence[Tuple[float, float]]] = None) -> np.ndarray:
    """Minimize ``cost_function`` starting from ``initial_guess``.

    Uses bounded L-BFGS-B when ``bounds`` are given, otherwise gradient-free
    Nelder-Mead, so the cost function does not need to be differentiable.
    """
    x0 = np.atleast_1d(np.asarray(initial_guess, dtype=float))
    method = "L-BFGS-B" if bounds is not None else "Nelder-Mead"
    result = minimize(cost_function, x0, method=method, bounds=bounds)
    return result.x
