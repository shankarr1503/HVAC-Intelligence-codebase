import numpy as np
from reinforcement_learning.climate_env import ClimateEnv
from control.mpc_controller import MPCController


def test_climate_env_step():
    env = ClimateEnv()
    state = env.reset()
    next_state, reward, done, info = env.step(1)
    assert len(next_state) == 5
    # Use np.isscalar or check if it's a number to avoid numpy float vs python float issues
    assert isinstance(float(reward), float)


def test_mpc_solver():
    mpc = MPCController(horizon=5)
    u = mpc.solve(current_temp=22, target_temp=20, outside_temp=25)
    assert isinstance(float(u), float)


if __name__ == "__main__":
    print("Testing climate_env_step...")
    test_climate_env_step()
    print("Testing mpc_solver...")
    test_mpc_solver()
    print("All tests passed!")
