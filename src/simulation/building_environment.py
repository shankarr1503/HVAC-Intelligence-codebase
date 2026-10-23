"""Representation of building thermal environment."""



class BuildingEnvironment:
    def __init__(self, volume: float = 100.0, outside_temp: float = 15.0):
        self.volume = volume
        self.outside_temp = outside_temp
        self.current_temp = outside_temp

    def step(self, hvac_power: float, dt: float = 1.0) -> float:
        """Advance environment by dt hours given hvac_power (-1 to 1 cooling/heating)."""
        # simple thermal inertia model
        self.current_temp += (self.outside_temp - self.current_temp) * 0.1 * dt
        self.current_temp += hvac_power * dt * 0.5
        return self.current_temp
