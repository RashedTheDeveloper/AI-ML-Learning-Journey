import numpy as np

scores = np.array([68, 69, 70, 71, 72])

mean = np.mean(scores)
variance = np.var(scores)
std = np.std(scores)

print("Scores:", scores)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std)

