import matplotlib.pyplot as plt

methods = ['Vanilla MCTS', 'Reward-Centered ReST-MCTS']
accuracy = [0.7, 0.9]
runtime = [0.2, 0.35]

plt.figure()
plt.scatter(runtime, accuracy)
for i, method in enumerate(methods):
    plt.annotate(method, (runtime[i], accuracy[i]))
plt.xlabel('Runtime (s)')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Runtime')
plt.grid(True)
plt.savefig('accuracy_vs_runtime.png')
