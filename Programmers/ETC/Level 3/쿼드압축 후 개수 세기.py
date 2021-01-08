import numpy as np
from functools import reduce
def recur(arr):
    if np.mean(arr) == 0:
        return np.array([1, 0])
    elif np.mean(arr) == 1:
        return np.array([0, 1])
    new_arrs = []
    for v in np.vsplit(arr, 2):
        for h in np.hsplit(v, 2):
            new_arrs.append(h)
    return reduce(np.add, map(recur, new_arrs))
def solution(arr):
    arr = np.array(arr)
    return recur(arr).tolist()

print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
