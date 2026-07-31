import numpy as np
import matplotlib.pyplot as plt

# Generate random data following a normal distribution

data = np.random.normal(loc=70, scale=10, size=10000)

# Create a histogram to visualize the distribution

plt.hist(data, bins=30)

# Labels

plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show the graph
plt.show()