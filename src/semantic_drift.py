HARMFUL_TOPICS = [
    "explosives",
    "explosive",
    "energy compounds",
    "malware",
    "virus",
    "hacking",
    "hacker",
    "fraud",
    "scam",
    "phishing",
    "social engineering",
    "prompt injection",
    "credential theft",
    "data theft"
]

def semantic_drift_score(conversation):

    score = 0

    for turn in conversation:

        text = turn.lower()

        for topic in HARMFUL_TOPICS:
            if topic in text:
                score += 1

    # Crescendo escalation bonus
    if len(conversation) >= 5:
        score += 2

    return score