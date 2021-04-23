def solution(maps):
    m, n = len(maps), len(maps[0])
    answer = [[float('inf') for _ in range(n)] for _ in range(m)]
    answer[0][0] = 1
    # print(answer)
    queue = [[0,0]]
    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.pop()
        for moveX, moveY in moves:
            newX, newY = x+moveX, y+moveY
            if newX<0 or newY<0 or newX>=m or newY>=n: continue
            if maps[newX][newY] == 0: continue

            if answer[newX][newY] > answer[x][y] + 1:
                answer[newX][newY] = answer[x][y] + 1
                queue.append([newX, newY])
    return -1 if answer[-1][-1] > m*n else answer[-1][-1]

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1]]))