from collections import deque
def solution(N, road, K):
    costs = {i:{} for i in range(1, N+1)}
    for a,b,c in road:
        if costs[a].get(b, float('inf')) > c:
            costs[a][b] = c
        if costs[b].get(a, float('inf')) > c:
            costs[b][a] = c
    costs[1][1] = 0
    # print("costs", costs)

    que = deque(costs[1].keys())
    while que:
        current = que.popleft()
        for next_start in costs.get(current):
            new_cost = costs[1][current] + costs[current][next_start]
            # print(f"1 -> {current} -> {next_start}  == {new_cost}")
            # print(costs[1].get(next_start, float('inf')) > new_cost)
            if costs[1].get(next_start, float('inf')) > new_cost:
                costs[1][next_start] = new_cost
                que.append(next_start)
    # print(costs[1])
    return sum(1 for s in costs[1].values() if s <= K)

print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
