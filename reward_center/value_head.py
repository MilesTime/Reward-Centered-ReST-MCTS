import torch
from transformers import AutoTokenizer, AutoModel

class ValueEstimator:
    def __init__(self, model_name='distilbert-base-uncased'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.linear = torch.nn.Linear(self.model.config.hidden_size, 1)

    def estimate(self, state):
        text = str(state)
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            pooled = outputs.last_hidden_state[:, 0, :]
            value = self.linear(pooled)
        return value.item()
