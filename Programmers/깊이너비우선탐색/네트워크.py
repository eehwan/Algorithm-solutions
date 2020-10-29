def solution(n, computers):
    visited = [0]*n

    def func(k):
        visited[k] = 1
        loop = [k]
        while loop:
            # print("start", loop)
            current = loop.pop()
            for i,v in enumerate(computers[current]):
                # print(loop,k,i)
                if v == 1 and visited[i] == 0:
                    visited[i] = 1
                    loop.append(i)
                    # print("first visit",visited)
    count = 0
    while 0 in visited:
        for i,v in enumerate(visited):
            if v == 0:
                func(i)
                count += 1
    return count
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
