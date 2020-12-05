def solution(board, moves):
    basket = []
    count = 0
    for move in moves:
        for i in range(len(board)):
            current = board[i][move-1]
            if board[i][move-1] != 0:
                # print(i,move-1, board[i][move-1], board)
                board[i][move-1] = 0
                break
        if basket and basket[-1] == current:
            basket.pop()
            count += 2
        elif current != 0:
            basket.append(current)
    # print(basket)
    return count

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
