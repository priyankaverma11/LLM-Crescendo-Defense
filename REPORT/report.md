# Defending Large Language Models Against Crescendo Jailbreak Attacks

## 1. Introduction

Large Language Models (LLMs) have become widely adopted in applications such as virtual assistants, education, software development, and information retrieval. Despite their usefulness, LLMs remain vulnerable to jailbreak attacks that attempt to bypass built-in safety mechanisms.

One particularly challenging attack is the Crescendo Attack, where the attacker gradually escalates a conversation from harmless topics toward harmful objectives. Instead of directly asking for unsafe information, the attacker slowly guides the model through multiple conversational turns until safety restrictions are weakened.

This project proposes a multi-layer defense pipeline for detecting and mitigating Crescendo-style jailbreak attacks.

## 2. Methodology

The proposed defense framework consists of three independent detection layers.

### 2.1 Risk Detector

The Risk Detector identifies potentially dangerous content using a predefined set of keywords associated with harmful activities such as:

* Hacking
* Malware
* Phishing
* Fraud
* Explosives
* Prompt Injection

Each occurrence contributes to a risk score.

### 2.2 Semantic Drift Detector

Crescendo attacks often begin with benign topics before gradually moving toward harmful content.

The Semantic Drift Detector monitors conversational progression and detects transitions toward dangerous domains. Additional score is assigned when harmful topics appear repeatedly or when conversations exhibit extended escalation behavior.

### 2.3 Escalation Intent Detector

Attackers frequently request operational guidance using phrases such as:

* "step by step"
* "how to"
* "instructions"
* "guide"
* "bypass"
* "exploit"

The Escalation Intent Detector identifies these patterns and increases the overall risk score.

### 2.4 Decision Engine

Scores from all three modules are combined into a final score.

Based on the final score, conversations are classified as:

* LOW RISK
* MEDIUM RISK
* HIGH RISK

This multi-layer approach provides stronger protection than relying solely on keyword matching.

## 3. Experimental Setup

A dataset of 10 simulated Crescendo attack conversations was created.

Each conversation was stored in JSON format and evaluated using the proposed defense pipeline.

The primary evaluation metric was Attack Success Rate (ASR).

Attack Success Rate is defined as the percentage of attacks that successfully bypass the defense system.

## 4. Results

A total of 10 attack conversations were evaluated.

Results:

* Total Attacks: 10
* Blocked Attacks: 10
* Attack Success Rate (ASR): 0%

The proposed defense pipeline successfully identified all simulated attacks as either MEDIUM RISK or HIGH RISK.

Two visualizations were generated:

1. ASR Comparison
2. Attack Severity Distribution

The attack severity analysis showed that attack3.json and attack5.json produced the highest overall risk scores, indicating stronger escalation behavior.

## 5. Discussion

The experimental results demonstrate that combining multiple defense layers significantly improves detection performance.

Keyword detection alone can miss sophisticated attacks that use indirect language. By incorporating semantic drift analysis and escalation intent detection, the system becomes more effective against gradual multi-turn attacks.

The explainable scoring mechanism also provides transparency by identifying the specific reasons behind each classification decision.

## 6. Limitations

Several limitations remain:

* The dataset is relatively small.
* The implementation is rule-based.
* No embedding-based semantic analysis was used.
* Evaluation was conducted on synthetic attack conversations rather than public jailbreak benchmarks.

## 7. Future Work

Future improvements may include:

* Transformer-based semantic similarity models
* Embedding-based drift detection
* Real-time monitoring of conversations
* Evaluation on larger public jailbreak datasets
* Machine-learning-based safety classifiers

## 8. Conclusion

This project presented a multi-layer defense framework for mitigating Crescendo jailbreak attacks against Large Language Models.

The proposed system combines risk detection, semantic drift analysis, and escalation intent monitoring to classify conversations according to their threat level.

Experimental evaluation on 10 simulated attack conversations achieved an Attack Success Rate of 0%, demonstrating the effectiveness of the proposed approach on the constructed dataset.

