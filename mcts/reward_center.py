import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class RewardingCenter:
    def __init__(self, model_name='mistralai/Mistral-7B-Instruct-v0.1'):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def rule_based(self, state):
        return 1.0 if 'valid' in state else -1.0

    def heuristic(self, state):
        return 0.5 if 'heuristic' in state else 0.0

    def neural_estimate(self, state):
        inputs = self.tokenizer(state, return_tensors="pt")
        outputs = self.model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss.item()
        return -loss  # Lower loss implies better state

    def compute_reward(self, state):
        alpha, beta, gamma = 0.5, 0.3, 0.2
        return alpha * self.rule_based(state) + \
               beta * self.heuristic(state) + \
               gamma * self.neural_estimate(state)
