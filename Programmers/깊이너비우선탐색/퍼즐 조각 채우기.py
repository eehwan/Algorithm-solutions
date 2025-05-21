from collections import deque

# 상하좌우 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 블록 또는 빈 공간 추출
def extract_shapes(board, target):
    n = len(board)
    visited = [[False]*n for _ in range(n)]
    shapes = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                shape = []

                while q:
                    x, y = q.popleft()
                    shape.append((x, y))
                    for dir in range(4):
                        nx, ny = x + dx[dir], y + dy[dir]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                # 기준점을 (0, 0)으로 맞추기
                min_x = min(pos[0] for pos in shape)
                min_y = min(pos[1] for pos in shape)
                normalized = sorted((x - min_x, y - min_y) for x, y in shape)
                shapes.append(normalized)
    return shapes

# 시계 방향 회전
def rotate(shape):
    return sorted((y, -x) for x, y in shape)

# 퍼즐을 채울 수 있는지 확인
def can_fill(empty, piece):
    for _ in range(4):
        if piece == empty:
            return True
        piece = rotate(piece)
        min_x = min(x for x, y in piece)
        min_y = min(y for x, y in piece)
        piece = sorted((x - min_x, y - min_y) for x, y in piece)
    return False

# 퍼즐 채우기
def puzzle_solution(game_board, table):
    n = len(game_board)
    empties = extract_shapes(game_board, 0)
    pieces = extract_shapes(table, 1)
    used = [False] * len(pieces)
    answer = 0

    for empty in empties:
        for i in range(len(pieces)):
            if used[i]:
                continue
            if len(empty) != len(pieces[i]):
                continue
            if can_fill(empty, pieces[i]):
                used[i] = True
                answer += len(empty)
                break

    return answer

# 테스트 케이스
game_board_1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table_1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

game_board_2 = [[0,0,0],[1,1,0],[1,1,1]]
table_2 = [[1,1,1],[1,0,0],[0,0,0]]

print(puzzle_solution(game_board_1, table_1), puzzle_solution(game_board_2, table_2))
