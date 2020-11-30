def solution(n):
    if n < 1 or type(n) is not int:
        return 0
    divisors = set()
    for i in range(1,int(n**0.5)+2):
        if n%i == 0:
            divisors |= {i, n//i}
    return sum([i for i in range(1,int(n**0.5)+2) if n%i == 0])

print(solution(0))
