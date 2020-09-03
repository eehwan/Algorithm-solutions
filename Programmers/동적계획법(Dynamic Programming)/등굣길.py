import numpy as np
def make_tiles(m,n,puddles):
    tiles = np.ones((n,m))
    for puddle in puddles:
        tiles[puddle[1]-1,puddle[0]-1] = 0
    return tiles
def min_arround(i,j,tiles):
    if tiles[i,j] == 0:
        return 0
    temp = 0
    if i>0:
        temp += tiles[i-1,j]
    if j>0:
        temp += tiles[i,j-1]
    print(i,j,temp)
    return temp
def solution(m, n, puddles):
    tiles = make_tiles(m,n,puddles)
    print(tiles)
    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0):
                continue
            # print(i,j)
            tiles[i,j] = min_arround(i,j,tiles)
    return tiles[n-1, m-1]%1000000007

test_case =\
"""
4, 3, [[2, 2]]
"""
expected_value =\
"""
4
"""

print(solution(\
4, 3, [[2, 2]]\
))
