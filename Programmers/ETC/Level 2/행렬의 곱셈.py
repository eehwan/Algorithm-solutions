import numpy as np
def solution(arr1, arr2):
    return np.array(arr1).dot(np.array(arr2)).tolist()

# numpy를 이용하지 않은 풀이
# def solution(arr1, arr2):
#     A = len(arr1)
#     B = len(arr1[0])
#     C = len(arr2[0])
#     return [[sum([arr1[idx1][idx3] * arr2[idx3][idx2] for idx3 in range(B)]) for idx2 in range(C)] for idx1 in range(A)]

# print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
