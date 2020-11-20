def solution(n):
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a+b
    return b % 1000000007

print(solution(5))
