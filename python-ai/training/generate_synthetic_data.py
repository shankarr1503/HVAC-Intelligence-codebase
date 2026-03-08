# generate_synthetic_data.py
"""Utility to run the cabin simulator and record data for model training."""

import csv
from simulation.cabin_thermal_simulator import simulate_step
import random


def create_dataset(filename: str, n: int = 1000):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cabin_temp','outside_temp','humidity','solar_radiation','vehicle_speed','passenger_count','battery_level','hvac_power','skin_temperature','heart_rate','seat_temperature','air_quality','next_temp'])
        # simple random walk
        cabin_temp = 22.0
        for i in range(n):
            outside_temp = random.uniform(-5,35)
            hvac = random.uniform(-1,1)
            solar = random.uniform(0,1)
            passenger_heat = random.uniform(0,0.5)
            next_temp = simulate_step(cabin_temp, outside_temp, hvac, solar, passenger_heat)
            row = [cabin_temp,outside_temp,random.uniform(20,80),solar,random.uniform(0,120),random.randint(1,4),random.uniform(0.2,1.0),hvac,random.uniform(30,36),random.uniform(60,100),random.uniform(20,30),random.uniform(0.5,1.0),next_temp]
            writer.writerow(row)
            cabin_temp = next_temp

if __name__ == '__main__':
    create_dataset('synthetic_data.csv', 5000)
