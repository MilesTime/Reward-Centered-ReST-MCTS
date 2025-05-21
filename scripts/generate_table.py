from baseline.vanilla_mcts import VanillaMCTS
from mcts.rest_mcts import RewardCenteredReSTMCTS
from data.sample_env import SampleEnv
from evaluation.metrics import evaluate

env = SampleEnv()
vanilla = VanillaMCTS(env)
rc_mcts = RewardCenteredReSTMCTS(env)

print("Vanilla MCTS")
print(evaluate(vanilla, [{"question": None, "answer": 'initial valid heuristic state'}]))

print("Reward-Centered ReST-MCTS")
print(evaluate(rc_mcts, [{"question": None, "answer": 'initial valid heuristic state'}]))
