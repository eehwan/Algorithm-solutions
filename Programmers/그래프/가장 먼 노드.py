from collections import deque

def solution(n, edge):
    queue = deque()
    queue.append(1)
    visited = {key:0 for key in edge}
    while queue:
        current = queue.popleft()
        for a,b in range(1,n+1):
            if visited(a) = 1:
                continue
            elif visited(b) = 1:
                continue
            else:

    return
