def solution(m, n, puddles):
    tiles = [[0]*(m+1) for _ in range(n+1)]
    print(tiles)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles:
                tiles[i][j] = 0
            elif (i,j) == (1, 1):
                tiles[i][j] = 1
            else:
                tiles[i][j] = tiles[i-1][j] + tiles[i][j-1]
    print(tiles)
    return tiles[n][m]%1000000007

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
