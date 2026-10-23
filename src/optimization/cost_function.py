"""Cost functions used by optimizers."""



def comfort_energy_cost(comfort_score: float, energy_use: float, alpha: float = 0.5) -> float:
    """Weighted cost of low comfort and high energy."""
    return alpha * (1.0 - comfort_score) + (1 - alpha) * energy_use
