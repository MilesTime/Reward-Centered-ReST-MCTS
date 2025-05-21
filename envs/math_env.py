class MathEnv:
    def initial_state(self):
        return {'expr': '2 * (3 + 4)', 'steps': [], 'depth': 0}

    def expand(self, state):
        expr = state['expr']
        options = [
            expr.replace('(3 + 4)', '7'),
            expr.replace('2 * (3 + 4)', '2 * 7'),
            expr.replace('2 * 7', '14')
        ]
        children = []
        for o in options:
            children.append({
                'expr': o,
                'steps': state['steps'] + [o],
                'depth': state['depth'] + 1
            })
        return children

    def is_terminal(self, state):
        return state['expr'] == '14'
