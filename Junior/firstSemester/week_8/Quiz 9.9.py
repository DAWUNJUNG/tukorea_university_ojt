import numpy as np
height = np.array([173, 168, 171, 189, 179])
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weight/(height**2)*10000
print(bmi)
