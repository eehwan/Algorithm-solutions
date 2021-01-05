def solution(board):
    n = len(board)
    hash = {i: {j: {'cost': float('inf'), 'dir': set()} for j in range(n)} for i in range(n)}
    hash[0][0]['cost'] = 0
    hash[0][0]['dir'] = {"hor", "ver"}

    stack = [(0,0)]
    def dir(current, next):
        if [a -b for a, b in zip(current, next)][0] in (-1, 1):
             return "ver"
        return "hor"
    while stack:
        current = stack.pop()
        if current == (n-1, n-1):
            continue
        a, b = current
        next_cords = []
        if a >= 0 and a <= n-2:
            next_cords.append((a+1, b))
        if a >= 1 and a <= n-1:
            next_cords.append((a-1, b))
        if b >= 0 and b <= n-2:
            next_cords.append((a, b+1))
        if b >= 1 and b <= n-1:
            next_cords.append((a, b-1))
        for q, w  in next_cords:
            if board[q][w] == 1:
                continue
            new_cost = hash[a][b]['cost'] + 100 if dir((a,b), (q,w)) in hash[a][b]['dir'] else hash[a][b]['cost'] + 600
            if new_cost < hash[q][w]['cost']:
                hash[q][w]['dir'] = set([dir((a,b), (q,w))])
                hash[q][w]['cost'] = new_cost
            elif new_cost == hash[q][w]['cost']:
                hash[q][w]['dir'].add(dir((a,b), (q,w)))
            else: continue
            # print((a,b),(q,w), new_cost)
            # print(hash[q][w]['dir'])
            stack.append((q, w))
    return hash[n-1][n-1]['cost']

print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))