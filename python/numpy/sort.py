import numpy as np

a = [5,3,7,1,2]

print("randam numbers:", a)

sorted_a = np.sort(a)
sorted_a_idx = np.argsort(a)

print("sorted_a:", sorted_a)
print("sorted_a_idx:", sorted_a_idx)
