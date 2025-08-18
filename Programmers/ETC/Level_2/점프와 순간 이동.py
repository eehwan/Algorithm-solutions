def solution(n):
    answer = 0
    while n != 0:
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    return answer
def solution1(n):
    return bin(n).count("1")

print(solution(4000))
