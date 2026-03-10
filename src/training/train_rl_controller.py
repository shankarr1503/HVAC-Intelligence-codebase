"""Example RL training loop using a simple gym environment."""
import gym
import numpy as np
from stable_baselines3 import PPO


def make_env():
    class SimpleHVACEnv(gym.Env):
        """Toy environment illustrating state-action-reward."""
        def __init__(self):
            super().__init__()
            # continuous 5-dim state
            self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(5,), dtype=np.float32)
            # action HVAC power level between -1 and 1
            self.action_space = gym.spaces.Box(low=-1, high=1, shape=(1,), dtype=np.float32)
            self.state = np.zeros(5)
            self.step_count = 0

        def reset(self):
            self.state = np.array([22.0, 10.0, 0.5, 1.0, 0.0], dtype=np.float32)
            self.step_count = 0
            return self.state

        def step(self, action):
            hvac_power = action[0]
            indoor, outdoor, hum, occ, energy = self.state
            # simple dynamics
            indoor += (outdoor - indoor) * 0.1 + hvac_power * 0.5
            energy = abs(hvac_power)
            # compute reward
            comfort_penalty = abs(indoor - 22.0) / 10.0
            reward = -0.5 * energy - 0.5 * comfort_penalty
            self.state = np.array([indoor, outdoor, hum, occ, energy], dtype=np.float32)
            self.step_count += 1
            done = self.step_count >= 100
            return self.state, reward, done, {}

    return SimpleHVACEnv()


def main():
    env = make_env()
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000)
    print("RL controller training complete")


if __name__ == '__main__':
    main()
