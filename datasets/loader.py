from datasets import load_dataset

def load_math_dataset(split='test'):
    ds = load_dataset("gsm8k", split=split)
    return [{"question": ex["question"], "answer": ex["answer"]} for ex in ds]
