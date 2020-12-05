def solution(n):
    if not isinstance(n, int) or n < 1:
        return 0
    divisors = set()
    for i in range(1,int(n**0.5)+2):
        if n%i == 0:
            divisors |= {i, n//i}
    return sum([i for i in range(1,int(n**0.5)+2) if n%i == 0])

print(solution(0))
