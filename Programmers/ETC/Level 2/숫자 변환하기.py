from collections import deque

def solution(x, y, n):
    queue = deque()
    if x == y:
        return 0
    visited = { x : 0 }
    queue.append(x)

    while queue:
        curr = queue.popleft()
        iter = visited[curr]
        next_items = [curr + n, curr * 2, curr * 3]
        for next in next_items:
            if next in visited:
                continue
            if next == y:
                return iter + 1
            elif next > y:
                continue

            queue.append(next)
            visited[next] = iter + 1
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
