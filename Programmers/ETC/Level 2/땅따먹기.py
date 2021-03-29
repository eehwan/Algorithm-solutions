import copy
def solution(land):
    # print(land)
    dp = copy.deepcopy(land)
    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if k != j:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])
    return max(dp[-1])

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))