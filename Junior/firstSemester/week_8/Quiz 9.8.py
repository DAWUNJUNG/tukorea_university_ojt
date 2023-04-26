import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70])
b = a[1:6:2]
print('b:', b)
b[1] = 10
print('b:', b)
print('a:', a)