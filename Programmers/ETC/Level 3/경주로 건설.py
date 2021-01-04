def solution(board):
    n = len(board)
    hash = [{i: {'num': float('inf'), 'ver': False, 'hor': False} for i in range(n)} for _ in range(n)]
    hash[0][num] = 0
    hash[0][ver] = True
    hash[0][hor] = True

    stack = [(0,0)]
    last = (0, 0)
    last_move = 0
    last_cost = 0
    while stack:
        current = stack.pop()
        print(current)
        a, b = current
        if a not in range(1, n) or b not in range(1, n):
            continue
        if board[a][b] == 1:
            continue

        move = "ver" if [a-b for a, b in zip(last, current)][0] in (-1, 1) else "hor"
        cost = last_cost + 100 if last_move == 0 or last_move == move else last_cost +500
        cost_map[a][b] = cost

        stack.append((a+1, b))
        stack.append((a-1, b))
        stack.append((a, b+1))
        stack.append((a, b-1))

        last = current
        last_move = move
    return hash

print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))