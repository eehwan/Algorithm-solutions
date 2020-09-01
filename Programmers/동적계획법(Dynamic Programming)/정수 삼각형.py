def solve(triangle):
    height = len(triangle)
    answer_list = triangle
    for i in range(height):
        for j in range(i+1):
            # print(i,j)
            if i == 0:
                pass
            elif j == 0:
                answer_list[i][j] = answer_list[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                answer_list[i][j] = answer_list[i-1][j-1] + triangle[i][j]
            else:
                answer_list[i][j] = max(answer_list[i-1][j-1],answer_list[i-1][j]) + triangle[i][j]
            # print(answer_list)
    return answer_list
def solution(triangle):
    return max(solve(triangle)[-1])

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
