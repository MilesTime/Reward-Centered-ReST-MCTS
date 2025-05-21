class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visit_count = 0
        self.value = 0.0
        self.reward = 0.0

    def add_child(self, child):
        self.children.append(child)

    def update(self, reward):
        self.visit_count += 1
        self.value += (reward - self.value) / self.visit_count
