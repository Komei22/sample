import numpy as np

a = np.array([1,1,1,2,3,4,5,1])

min_idx = np.where(a == a.min())

print(min_idx)
