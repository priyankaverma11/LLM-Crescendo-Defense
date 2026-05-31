# LLM-Crescendo-Defense


## Overview

This project implements a multi-layer defense pipeline against Crescendo-style jailbreak attacks targeting Large Language Models (LLMs).

The system combines:

* Risk Detection
* Semantic Drift Detection
* Escalation Intent Detection

to identify and block potentially harmful multi-turn conversations.

---

## Project Structure

```text
LLM-Crescendo-Defense/

├── attacks/
├── src/
├── results/
├── README.md
├── REPORT/
│   └── report.md
├── requirements.txt
└── venv/
```

---

## Defense Pipeline

Conversation
↓
Risk Detector
↓
Semantic Drift Detector
↓
Escalation Intent Detector
↓
Risk Classification
↓
LOW / MEDIUM / HIGH RISK

---

## Evaluation

Dataset:

* 10 simulated Crescendo attack conversations

Metrics:

* Attack Success Rate (ASR)

Results:

| Metric          | Value |
| --------------- | ----- |
| Total Attacks   | 10    |
| Blocked Attacks | 10    |
| ASR             | 0%    |

---

## Generated Outputs

The results folder contains:

* attack_results.csv
* asr_comparison.png
* attack_severity.png
* results.txt

---

## Running the Project

```bash
cd src

python3 evaluate_attacks.py

python3 export_results.py

python3 plot_results.py

python3 plot_attack_scores.py
```

---

## Future Work

* Embedding-based semantic analysis
* Transformer-based classifiers
* Real-world jailbreak datasets
* Real-time monitoring systems
