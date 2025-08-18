from collections import deque

def solution(x, y, n):
    if x == y:
        return 0

    queue = deque([x])
    visited = {x: 0}

    while queue:
        cur = queue.popleft()
        steps = visited[cur]

        nexts = [cur + n, cur * 2, cur * 3]
        for nxt in nexts:
            if nxt == y:
                return steps + 1
            if nxt > y or nxt in visited:
                continue

            visited[nxt] = steps + 1
            queue.append(nxt)

    return -1
    

if __name__ == "__main__":
    test_cases = [
        [10, 40, 5],        # 2
        [10, 40, 30],       # 1
        [2, 5, 4],          # -1
        [5, 5, 5],          # 0
        [5, 1000000, 3]     # 22
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
