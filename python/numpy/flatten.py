import numpy as np

a = np.arange(10).reshape(10,1)

print("元:\n", type(a))

b = a.flatten()

print("flatten後:\n", b)
