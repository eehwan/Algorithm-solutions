def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    print(costs)
    visited_islands = set([0])
    answer = 0
    while len(visited_islands) != n:
        for element in costs:
            start, end, cost = element
            if start in visited_islands or end in visited_islands:
                if start in visited_islands and end in visited_islands:
                    continue
                else:
                    visited_islands |= {start, end}
                    answer += cost
                    # print("added")
                    # print(f"loop : {element}")
                    # print(f"visited_islands : {visited_islands}")
                    break
    return answer


test_case =\
"""
4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]
6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]]
5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
4, [[2, 3, 3], [2, 4, 4], [3, 4, 7], [3, 5, 3], [4, 5, 10]]
5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]
"""
expected_value =\
"""
4
104
11
9
7
8
10
7
"""

answer = solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])
print(answer)
