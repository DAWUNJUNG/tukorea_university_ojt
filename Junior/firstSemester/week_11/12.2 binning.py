import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.hist(x, density=True, bins=np.linspace(-5, 5, 21))
plt.show()