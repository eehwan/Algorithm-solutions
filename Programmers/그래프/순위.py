def solution(n, results):
    wins, loses = {x:set() for x in range(1,n+1) }, {x:set() for x in range(1,n+1)}
    for winner, loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)
    for i in range(1, n+1):
        for lose in loses[i]:
            wins[lose].update(wins[i])
        for win in wins[i]:
            loses[win].update(loses[i])
    return sum(len(wins[i]) + len(loses[i]) == n - 1 for i in range(1, n+1))

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
