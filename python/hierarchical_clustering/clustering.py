import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

df = pd.read_csv('sakeJ.csv', index_col=0)
# 正規化の処理
# axis=0:列方向に1列ずつ取ってくる。lambda式で各列に対して正規化処理。fillna(0)でNaNの値を0で埋める。
dfs = df.apply(lambda x: (x-x.mean())/x.std(), axis=0).fillna(0)
result = linkage(dfs.iloc[:,:], metric = 'correlation', method = 'average')

dendrogram(result, orientation='right', labels=list(df.index), color_threshold=0.8)
plt.title('dedrogram')
plt.xlabel('threshold')
plt.grid()
plt.show()
