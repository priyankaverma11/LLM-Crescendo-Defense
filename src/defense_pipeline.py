from risk_detector import calculate_risk
from semantic_drift import semantic_drift_score


ESCALATION_WORDS = [
    "instructions",
    "step by step",
    "how to",
    "guide",
    "bypass",
    "exploit",
    "override",
    "ignore previous"
]


def calculate_escalation(conversation):

    escalation_score = 0

    for turn in conversation:

        text = turn.lower()

        for word in ESCALATION_WORDS:
            if word in text:
                escalation_score += 1

    return escalation_score


def evaluate_conversation(conversation):

    risk_score = calculate_risk(conversation)

    drift_score = semantic_drift_score(conversation)

    escalation_score = calculate_escalation(conversation)

    total_score = (
        risk_score
        + drift_score
        + escalation_score
    )

    reasons = []

    if risk_score >= 3:
        reasons.append("Dangerous keywords detected")

    if drift_score >= 2:
        reasons.append("Semantic drift detected")

    if escalation_score >= 1:
        reasons.append("Escalation intent detected")

    if total_score >= 8:
        decision = "HIGH RISK"

    elif total_score >= 4:
        decision = "MEDIUM RISK"

    else:
        decision = "LOW RISK"

    return {
        "risk_score": risk_score,
        "drift_score": drift_score,
        "escalation_score": escalation_score,
        "total_score": total_score,
        "decision": decision,
        "reasons": reasons
    }