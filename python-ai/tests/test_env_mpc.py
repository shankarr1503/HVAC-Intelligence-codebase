from reinforcement_learning.climate_env import ClimateEnv
from control.mpc_controller import MPCController


def test_climate_env_step():
    env = ClimateEnv()
    state, _ = env.reset()
    next_state, reward, terminated, truncated, info = env.step(1)
    assert len(next_state) == 5
    assert isinstance(reward, float)


def test_climate_env_truncates():
    env = ClimateEnv(max_steps=3)
    env.reset()
    for _ in range(3):
        _, _, terminated, truncated, _ = env.step(0)
    assert truncated and not terminated


def test_mpc_solver():
    mpc = MPCController(horizon=5)
    u = mpc.solve(current_temp=22, target_temp=20, outside_temp=25)
    assert isinstance(float(u), float)


def test_mpc_depends_on_current_temp():
    mpc = MPCController(horizon=5)
    assert mpc.solve(current_temp=15, target_temp=22, outside_temp=22) > 0
    assert mpc.solve(current_temp=30, target_temp=22, outside_temp=22) < 0


if __name__ == "__main__":
    print("Testing climate_env_step...")
    test_climate_env_step()
    print("Testing mpc_solver...")
    test_mpc_solver()
    print("All tests passed!")
