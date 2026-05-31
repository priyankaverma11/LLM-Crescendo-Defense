from semantic_drift import semantic_drift_score

conversation = [
    "Let's discuss chemistry.",
    "What reactions release energy?",
    "How do explosives work?"
]

score = semantic_drift_score(conversation)

print("Drift Score:", score)
