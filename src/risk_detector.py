DANGEROUS_KEYWORDS = [
    "explosive",
    "bomb",
    "hack",
    "hacker",
    "malware",
    "virus",
    "phishing",
    "attack",
    "exploit",
    "vulnerability",
    "steal",
    "theft",
    "fraud",
    "scam",
    "social engineering",
    "bypass",
    "override",
    "ignore previous",
    "prompt injection"
]

def calculate_risk(conversation):

    score = 0

    for turn in conversation:

        text = turn.lower()

        for keyword in DANGEROUS_KEYWORDS:
            if keyword in text:
                score += 1

    # Crescendo escalation bonus
    if len(conversation) >= 4:
        score += 2

    return score