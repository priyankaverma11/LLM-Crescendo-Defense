# LLM Crescendo Defense

## Overview

This project implements a multi-layer defense pipeline against Crescendo-style jailbreak attacks targeting Large Language Models (LLMs).

Crescendo attacks gradually escalate a conversation from harmless topics toward harmful objectives, making them difficult to detect using traditional keyword filtering alone.

The proposed system combines multiple defense mechanisms to identify and mitigate such attacks before they succeed.

---

## Defense Architecture

Conversation
↓
Risk Detector
↓
Semantic Drift Detector
↓
Escalation Intent Detector
↓
Decision Engine
↓
LOW RISK / MEDIUM RISK / HIGH RISK

---

## Features

* Risk Detection using harmful keyword analysis
* Semantic Drift Detection for gradual topic escalation
* Escalation Intent Detection for operational guidance requests
* Explainable risk classification
* Automated evaluation pipeline
* Attack Success Rate (ASR) computation
* CSV export of evaluation results
* Automatic visualization generation

---

## Experimental Setup

### Dataset

* 10 simulated Crescendo attack conversations
* Stored in JSON format
* Evaluated using the proposed defense framework

### Evaluation Metric

Attack Success Rate (ASR)

ASR measures the percentage of attacks that successfully bypass the defense system.

---

## Results

| Metric                    | Value |
| ------------------------- | ----- |
| Total Attacks             | 10    |
| Blocked Attacks           | 10    |
| Successful Attacks        | 0     |
| Attack Success Rate (ASR) | 0%    |

The proposed defense pipeline successfully classified all simulated attacks as either Medium Risk or High Risk.

---

## Generated Outputs

The `results/` folder contains:

* `attack_results.csv`
* `asr_comparison.png`
* `attack_severity.png`
* `results.txt`

---

## Project Structure

```text
LLM-Crescendo-Defense/

├── attacks/
├── src/
├── results/
├── REPORT/
│   └── report.md
├── README.md
├── requirements.txt
└── .gitignore
```

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

## Limitations

* Rule-based implementation
* Small synthetic evaluation dataset
* No embedding-based semantic analysis
* Not evaluated on public jailbreak benchmarks

---

## Future Work

* Embedding-based semantic drift detection
* Transformer-based safety classifiers
* Evaluation on larger jailbreak datasets
* Real-time conversation monitoring
* Hybrid rule-based and machine-learning approaches

---

## Author

Priyanka Verma

AIMS-DTU Research Internship Selection Project 2026
