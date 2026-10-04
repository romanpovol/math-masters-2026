import numpy as np, matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Read input
x = np.array(list(map(float, input().split())))

# Evaluation points
xx = np.linspace(x.min(), x.max(), 1000)

# Plot KDE
plt.plot(xx, gaussian_kde(x)(xx))
plt.show()
