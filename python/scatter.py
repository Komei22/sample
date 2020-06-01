import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

x = y = np.arange(5)

fig, ax = plt.subplots(1)

ax.scatter(x, y,  s=100, marker='x', color='b', linewidth=1)
ax.scatter(x, y+1, s=100, marker='x', color='r', linewidth=2)
ax.scatter(x, y+2, s=100, marker='x', color='g', linewidth=3)

plt.show()
