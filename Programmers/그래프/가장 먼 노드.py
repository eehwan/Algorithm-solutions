from collections import deque

def solution(n, edge):
    graph = {key:[] for key in range(1,n+1)}
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = {key: False for key in range(2, n+1)}
    visited[1] = True

    queue = deque([1])
    answer = 1      # 거리가 현재 길이인 노드의 갯수
    while queue:
        answer = len(queue)
        for _ in range(answer):
            node = queue.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

    return answer

if __name__ == "__main__":
    test_cases = [
        [6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]],  # 3
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")