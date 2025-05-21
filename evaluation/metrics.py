from time import time

def evaluate(mcts, dataset):
    correct = 0
    total_time = 0
    for ex in dataset:
        start = time()
        pred = mcts.search(question=ex["question"])
        total_time += time() - start
        if pred == ex["answer"]:
            correct += 1
    return {
        'accuracy': correct / len(dataset),
        'avg_runtime': total_time / len(dataset)
    }
