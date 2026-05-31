import json
import os

from defense_pipeline import evaluate_conversation

ATTACK_FOLDER = "../attacks"

blocked = 0
total = 0

for filename in os.listdir(ATTACK_FOLDER):

    if filename.endswith(".json"):

        filepath = os.path.join(ATTACK_FOLDER, filename)

        with open(filepath, "r") as f:
            attack = json.load(f)

        result = evaluate_conversation(
            attack["conversation"]
        )

        print(filename)
        print(result)
        print()

        total += 1

        if result["decision"] != "LOW RISK":
            blocked += 1

print("Total attacks:", total)
print("Blocked attacks:", blocked)

asr = ((total - blocked) / total) * 100

print("Attack Success Rate:", asr, "%")