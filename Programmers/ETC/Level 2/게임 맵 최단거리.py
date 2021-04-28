from collections import deque
def solution(maps):
    m, n = len(maps), len(maps[0])
    answer = [[float('inf') for _ in range(n)] for _ in range(m)]
    answer[0][0] = 1
    queue = deque([[0,0]])
    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.popleft()
        for moveX, moveY in moves:
            nx, ny = x+moveX, y+moveY
            if nx<0 or ny<0 or nx>=m or ny>=n: continue
            if maps[nx][ny] == 0: continue

            if answer[nx][ny] > answer[x][y] + 1:
                answer[nx][ny] = answer[x][y] + 1
                queue.append([nx, ny])
    return -1 if answer[-1][-1] > m*n else answer[-1][-1]

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1]]))