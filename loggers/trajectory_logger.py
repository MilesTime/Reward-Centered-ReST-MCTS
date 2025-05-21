class Logger:
    def __init__(self):
        self.paths = []

    def log(self, state, reward, value):
        self.paths.append((str(state), reward, value))

    def dump(self, path='log.txt'):
        with open(path, 'w') as f:
            for s, r, v in self.paths:
                f.write(f'{s} | Rc: {r:.2f} | V(s): {v:.2f}\n')
