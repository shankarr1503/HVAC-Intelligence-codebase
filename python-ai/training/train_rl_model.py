# train_rl_model.py
"""Script to train the RL HVAC controller."""

from reinforcement_learning.climate_env import ClimateEnv
from reinforcement_learning.hvac_rl_controller import train_rl


def main():
    env = ClimateEnv()
    model = train_rl(env, timesteps=10000)
    model.save("hvac_agent.zip")


if __name__ == "__main__":
    main()
