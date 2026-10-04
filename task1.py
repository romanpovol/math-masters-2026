import numpy as np, matplotlib.pyplot as plt

# Read input
x = np.sort(np.array(list(map(float, input().split()))))
p = float(input())

# Plot Empirical Cumulative Distribution Function
plt.ecdf(x)
plt.show()

# Calculate quantile
print(np.quantile(x, p, method="inverted_cdf"))
