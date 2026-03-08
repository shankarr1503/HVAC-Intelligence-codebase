# climate_env.py
"""Gym environment for HVAC RL agent."""

import gym
from gym import spaces
import numpy as np


class ClimateEnv(gym.Env):
    def __init__(self):
        super().__init__()
        # state: cabin_temp, humidity, comfort_score, battery_level, outside_temp
        self.observation_space = spaces.Box(low=np.array([0,0,0,0, -50],dtype=np.float32),
                                           high=np.array([50,100,1,1,50],dtype=np.float32))
        # actions: off, cool_low, cool_med, cool_high, heat
        self.action_space = spaces.Discrete(5)
        self.state = None
        self.battery_usage = 0.0

    def reset(self):
        self.state = np.array([22.0, 40.0, 0.5, 0.8, 15.0], dtype=np.float32)
        self.battery_usage = 0.0
        return self.state

    def step(self, action):
        cabin, hum, comfort, batt, outside = self.state
        # simple thermal dynamics
        hvac_power = 0.0
        if action == 1:
            hvac_power = -0.5
        elif action == 2:
            hvac_power = -1.0
        elif action == 3:
            hvac_power = -1.5
        elif action == 4:
            hvac_power = 1.0
        # update cabin temp
        delta = (outside - cabin) * 0.1 + hvac_power * 0.1
        cabin = cabin + delta
        # update comfort score using previous formula
        comfort = max(0.0, 1.0 - abs(cabin - 22.0) / 10.0)
        # battery drains proportional to hvac_power magnitude
        batt = max(0.0, batt - abs(hvac_power) * 0.01)
        self.battery_usage += abs(hvac_power) * 0.01
        self.state = np.array([cabin, hum, comfort, batt, outside], dtype=np.float32)
        # reward: comfort reward minus energy penalty
        reward = comfort - 0.5 * abs(hvac_power)
        done = batt <= 0.0
        info = {"hvac_power": hvac_power}
        return self.state, reward, done, info
