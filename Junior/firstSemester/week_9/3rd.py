import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x**2.0
plt.plot(x, y, "bo-", linewidth=3, markersize=5)
plt.show()