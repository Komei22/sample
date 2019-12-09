import numpy as np

M = np.array(
    [[1, 2],
     [3, 4],
     [5, 6]]
)

# argmax()は2次元の場合flatten()で一次元に直したときのidxを返す。shapeは行列の形をとってくる。unrabel_index()はargmax()の結果をshapeに合わせて変換している。
max_idx = np.unravel_index(M.argmax(), M.shape)

print(max_idx)
