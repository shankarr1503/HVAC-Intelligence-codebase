# hvac_rl_controller.py
"""Wrapper around Stable-Baselines3 PPO for HVAC control."""

from stable_baselines3 import PPO
from .climate_env import ClimateEnv


def train_rl(env: ClimateEnv, timesteps: int = 10000):
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=timesteps)
    return model


def load_model(path: str):
    return PPO.load(path)


def select_action(model, state):
    action, _ = model.predict(state)
    return action
