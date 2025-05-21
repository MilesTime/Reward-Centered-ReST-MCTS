class SampleEnv:
    def initial_state(self):
        return 'initial valid heuristic state'

    def expand(self, state):
        return [state + '->next1', state + '->next2']

    def is_terminal(self, state):
        return 'next2' in state
