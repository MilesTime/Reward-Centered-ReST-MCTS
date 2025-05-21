# Reward-Centered ReST-MCTS

This repository contains the official implementation of the arXiv:2503.05226 [cs.RO] submission:

**Reward-Centered ReST-MCTS: A Robust Decision-Making Framework for Robotic Manipulation in High Uncertainty Environments**

## 🔧 Features
- Monte Carlo Tree Search with Intermediate Reward Shaping
- Integration with Huggingface Transformers (Mistral-7B)
- Reproduction of benchmark results (Table II/III in paper)

## 🚀 Installation
```bash
pip install -r requirements.txt
```

## 📦 Datasets
GSM8K via Huggingface Datasets is used to simulate math reasoning (replaceable with MATH, GPQA, etc.):
```python
from datasets.loader import load_math_dataset
```

## 🔁 Run Example
```bash
python main.py
```

## 📊 Run Experiments
```bash
python scripts/run_experiments.py
python scripts/generate_table.py
python plot/plot_accuracy_vs_runtime.py
```

## 🧪 Baselines
- Vanilla MCTS: `baseline/vanilla_mcts.py`
- Reward-Centered ReST-MCTS: `mcts/rest_mcts.py`

## 📄 Paper-to-Code Mapping
| Paper Component | Code Location |
|------------------|----------------|
| Algorithm 1      | `rest_mcts.py` |
| Eq(1-3)          | `reward_center.py` |
| Table II/III     | `generate_table.py` |
| Fig 2            | `plot_accuracy_vs_runtime.py` |

## 📬 Contact
For any issues or questions, please contact: xwan0575@uni.sydney.edu.au


## 🔍 Deep Features for arXiv:2503.05226 [cs.RO]

This version includes:

- `envs/math_env.py`: A toy but logic-representative math environment with multi-step reasoning paths and ambiguity.
- `reward_center/value_head.py`: A transformer-based value estimator (state to scalar Rc(s) score).
- `loggers/trajectory_logger.py`: Logs each search path with reward and value information.
- Pruning mechanism: Tree search favors higher Rc and prunes incorrect intermediate expansions.

