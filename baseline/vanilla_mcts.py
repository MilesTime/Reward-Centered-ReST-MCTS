from mcts.tree_node import TreeNode

class VanillaMCTS:
    def __init__(self, env, simulations=50):
        self.env = env
        self.simulations = simulations

    def search(self, question=None):
        root = TreeNode(self.env.initial_state())
        for _ in range(self.simulations):
            node = root
            while not self.env.is_terminal(node.state):
                next_states = self.env.expand(node.state)
                node = TreeNode(next_states[0], parent=node)  # pick first
            node.update(1.0)
        return root.state
