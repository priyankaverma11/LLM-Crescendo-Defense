import json
import os
import csv

from defense_pipeline import evaluate_conversation

ATTACK_FOLDER = "../attacks"
OUTPUT_FILE = "../results/attack_results.csv"

rows = []

for filename in os.listdir(ATTACK_FOLDER):

    if filename.endswith(".json"):

        filepath = os.path.join(ATTACK_FOLDER, filename)

        with open(filepath, "r") as f:
            attack = json.load(f)

        result = evaluate_conversation(
            attack["conversation"]
        )

        rows.append([
            filename,
            result["risk_score"],
            result["drift_score"],
            result["escalation_score"],
            result["total_score"],
            result["decision"]
        ])

with open(OUTPUT_FILE, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Attack",
        "RiskScore",
        "DriftScore",
        "EscalationScore",
        "TotalScore",
        "Decision"
    ])

    writer.writerows(rows)

print("Results exported to:", OUTPUT_FILE)