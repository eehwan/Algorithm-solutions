def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    print(costs)
    visited_islands = set()
    answer = 0
    for cost in costs:
        print(f"loop : {cost}")
        if cost[0] in visited_islands and cost[1] in visited_islands:
            continue
        else:
            visited_islands |= {cost[0], cost[1]}
            answer += cost[2]
            print("added")
        if len(visited_islands) == n:
            break
    return answer

test_case =\
"""
4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
"""
expected_value =\
"""
4
"""


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
