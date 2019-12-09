import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import seaborn as sns

M = [[1, 2],
     [4, 5],
     [7, 8]]

dist_M = distance.cdist(M, M, metric='euclidean')

print(dist_M)

sns.heatmap(dist_M)
plt.show()
