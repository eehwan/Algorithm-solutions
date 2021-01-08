import numpy as np
def recur(arr):
    if np.mean(arr) == 0:
        return np.array([1, 0])
    elif np.mean(arr) == 1:
        return np.array([0, 1])
    new_arrs = []
    for v in np.vsplit(arr, 2):
        for h in np.hsplit(v, 2):
            new_arrs.append(h)
    total = np.array([0, 0])
    for new_arr in new_arrs:
        total = np.sum((total, recur(new_arr)), axis=0)
    return total.tolist()
def solution(arr):
    arr = np.array(arr)
    return recur(arr)

print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
