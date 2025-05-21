import math
from mcts.tree_node import TreeNode
from mcts.reward_center import RewardingCenter

class RewardCenteredReSTMCTS:
    def __init__(self, env, simulations=50):
        self.env = env
        self.simulations = simulations
        self.rewarding_center = RewardingCenter()

    def search(self):
        root = TreeNode(self.env.initial_state())
        for _ in range(self.simulations):
            node = root
            path = [node]
            while node.children:
                node = self.select(node)
                path.append(node)
            if not self.env.is_terminal(node.state):
                new_states = self.env.expand(node.state)
                for state in new_states:
                    child = TreeNode(state, parent=node)
                    child.reward = self.rewarding_center.compute_reward(state)
                    node.add_child(child)
            reward = path[-1].reward
            for n in reversed(path):
                n.update(reward)
        return max(root.children, key=lambda x: x.value).state

    def select(self, node):
        log_n = math.log(node.visit_count + 1)
        return max(node.children, key=lambda c: c.value + math.sqrt(log_n / (c.visit_count + 1)))
