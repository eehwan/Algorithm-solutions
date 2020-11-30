def solution(n):
    new_n = ""          # 3진법 역순배
    while n:
        new_n += str(n%3)
        n //= 3
    answer = 0
    for i, v in enumerate(str(int(new_n))[::-1]):
        answer += 3**i * int(v)
    return answer

print(solution(125))
