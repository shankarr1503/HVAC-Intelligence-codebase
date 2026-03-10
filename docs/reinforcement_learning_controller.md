# Reinforcement Learning Controller

The RL controller interacts with a simulated or real environment to learn
control policies that balance comfort and energy efficiency.

The current implementation (`src/controllers/reinforcement_learning_controller.py`)
provides a stub with a `select_action` method and a `policy` attribute that can
be set to any callable taking a state vector. Training algorithms such as
stable-baselines3 agents can be integrated by replacing the stub with concrete
policy update code.

### Workflow
1. Initialize environment (e.g., `BuildingEnvironment`).
2. Create RL agent and wrap it in `RLController`.
3. Collect experiences during simulation episodes.
4. Update policy with reinforcement learning algorithm (e.g., PPO, DQN).

### Customization
The `update_policy` method is a placeholder where developers should implement
training logic or reload a pre-trained model. This design keeps the controller
agnostic to the underlying RL library.
