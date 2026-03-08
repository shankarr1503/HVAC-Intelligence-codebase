# cabin_thermal_simulator.py
"""Physics-based cabin temperature simulator."""


def simulate_step(cabin_temp: float, outside_temp: float, hvac_power: float, solar_heat: float, passenger_heat: float) -> float:
    # simple thermal model: cabin_temp += (outside_temp - cabin_temp)*0.1 + hvac_power*0.05 + solar_heat*0.02 + passenger_heat*0.01
    delta = (outside_temp - cabin_temp) * 0.1 + hvac_power * 0.05 + solar_heat * 0.02 + passenger_heat * 0.01
    return cabin_temp + delta
