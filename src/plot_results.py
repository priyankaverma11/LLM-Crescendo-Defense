import matplotlib.pyplot as plt

methods = [
    "Baseline",
    "Defense Pipeline"
]

asr = [
    100,
    20
]

plt.bar(methods, asr)

plt.ylabel("Attack Success Rate (%)")

plt.title("Defense Performance")

plt.savefig("../results/asr_comparison.png")

plt.show()