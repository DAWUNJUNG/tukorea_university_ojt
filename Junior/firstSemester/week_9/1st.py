import numpy as np
import matplotlib.pyplot as plt

points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])

p = np.array([2.5, 2])
plt.plot(points[:, 0], points[:, 1], "ro")
plt.plot(p[0], p[1], "bo")
plt.show()