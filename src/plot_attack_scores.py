import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/attack_results.csv")

plt.figure(figsize=(10,5))

plt.bar(df["Attack"], df["TotalScore"])

plt.ylabel("Total Score")
plt.xlabel("Attack")
plt.title("Attack Severity Distribution")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../results/attack_severity.png")

plt.show()