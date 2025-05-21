from mcts.rest_mcts import RewardCenteredReSTMCTS
from data.sample_env import SampleEnv

if __name__ == '__main__':
    env = SampleEnv()
    mcts = RewardCenteredReSTMCTS(env)
    best_trajectory = mcts.search()
    print("Best Trajectory:", best_trajectory)
