import numpy as np
import itertools
import matplotlib.pyplot as plt
x = np.random.rand(100)
y = np.random.rand(100)
colors = itertools.cycle(["red", "green", "blue", "yellow", "pink", "orange", "purple", "brown", "cyan", "magenta"])
colors = [next(colors) for _ in range(100)]
shape = np.pi * (np.random.rand(100)*20) **2
plt.scatter(x, y, s=shape, c=colors, marker='o', alpha=0.5)
plt.show()