from collections import deque

def get_group_sizes(n, wires):
    """전선 정보에서 연결된 두 그룹의 크기를 찾아 반환"""
    graph = {i: set() for i in range(1, n + 1)}
    for x, y in wires:
        graph[x].add(y)
        graph[y].add(x)

    visited = set()
    group_sizes = []

    for node in graph:
        if node not in visited:
            queue = deque([node])
            group_size = 0

            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    group_size += 1
                    queue.extend(graph[current] - visited)

            group_sizes.append(group_size)

    return group_sizes  # 두 그룹의 크기 리스트 반환

def solution(n, wires):
    """전선 하나를 제거했을 때 두 그룹의 크기 차이가 최소가 되는 값을 반환"""
    answer = float('inf')

    for i in range(n - 1):
        new_wires = [w for j, w in enumerate(wires) if j != i]  # i번째 전선 제거
        group_sizes = get_group_sizes(n, new_wires)
        difference = abs(group_sizes[0] - group_sizes[1])
        answer = min(difference, answer)

    return answer
