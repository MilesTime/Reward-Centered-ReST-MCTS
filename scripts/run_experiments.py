from mcts.rest_mcts import RewardCenteredReSTMCTS
from datasets.loader import load_math_dataset
from evaluation.metrics import evaluate
from data.sample_env import SampleEnv

if __name__ == '__main__':
    dataset = load_math_dataset(split='test[:10]')  # limit for speed
    env = SampleEnv()
    mcts = RewardCenteredReSTMCTS(env)
    results = evaluate(mcts, dataset)
    print("Evaluation Results:", results)
