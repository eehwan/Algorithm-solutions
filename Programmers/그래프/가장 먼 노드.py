def solution(n, edge):
    queue, queue2 = [1], set()
    node = {key:[] for key in range(1,n+1)}
    for a, b in edge:
        node[a].append(b)
        node[b].append(a)
    visited = {key:0 for key in range(2, n+1)}
    visited[1] = 1
    while queue:
        for current in queue:
            print(queue)
            for destination in node[current]:
                if visited[destination] == 0:
                    queue2.add(destination)
                    visited[destination] = 1
                print(current, destination, visited, queue2)
        if queue2 == set():
            break
        queue, queue2 = list(queue2), set()
    return len(queue)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
