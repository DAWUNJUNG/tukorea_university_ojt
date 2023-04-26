import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(30)
y = np.random.rand(30)
colors = np.random.rand(30)
size = np.pi * (np.random.rand(30)*20) **2
plt.scatter(x, y, s=size, c = colors, marker='*', alpha=0.7)
plt.show()