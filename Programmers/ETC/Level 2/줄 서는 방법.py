from itertools import permutations
def solution(n, k):
    i = 0
    for a, b, c in permutations([i for i in range(1, n+1)], n):
        i += 1
        if i == k:
            return [a, b, c]

print(solution(3, 5))