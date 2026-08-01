import numpy as np
import matplotlib.pyplot as plt

# Same mean, different standard deviation

np.random.seed(42)

data_small = np.random.normal(loc=70, scale=2, size=1000)
data_large = np.random.normal(loc=70, scale=15, size=1000)

plt.figure(figsize=(10,5))

plt.hist(data_small, bins=30, alpha=0.7, label="Std = 2")

plt.hist(data_large, bins=30, alpha=0.7, label="Std = 15")

plt.title("Small vs Large Standard Deviation")

plt.xlabel("Scores")

plt.ylabel("Frequency")

plt.legend()

plt.savefig("images/small_vs_large_std.png")

plt.show()