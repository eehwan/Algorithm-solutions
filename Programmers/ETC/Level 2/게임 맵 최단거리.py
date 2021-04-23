def solution(maps):
    m, n = len(maps), len(maps[0])
    answer = [[float('inf') for _ in range(n)] for _ in range(m)]
    print(answer)
    queue = [[0,0]]
    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.pop()
        if x<0 or y<0 or x>=m or y>=n:
            continue
        if maps[x][y] == 0: continue
        for moveX, moveY in moves:
            queue.append(x+moveX, y+moveY)
    return -1 if answer[-1][-1] == 0 else answer[-1][-1]