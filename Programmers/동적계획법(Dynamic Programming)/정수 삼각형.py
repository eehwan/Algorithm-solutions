def solve(triangle,m,n):
    now = triangle[m][n]
    # print(m,n,now)
    if m == 0:
        return now
    if n == 0:
        answer = solve(triangle,m-1,n) + now
        # print(answer)
        return answer
    if n == len(triangle[m])-1:
        answer = solve(triangle,m-1,n-1) + now
        # print(answer)
        return answer
    answer = max(solve(triangle,m-1,n-1),solve(triangle,m-1,n)) + now
    # print(answer)
    return answer
def solution(triangle):
    m = len(triangle)
    n = len(triangle[-1])
    return max(solve(triangle,m-1,i) for i in range(n))

test_case =\
"""
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
"""
expected_value =\
"""
30
"""

print(solution(\
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]\
))
