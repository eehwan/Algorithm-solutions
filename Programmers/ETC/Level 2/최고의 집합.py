def solution(n, s):
    answer = []
    while n:
        temp = s//n
        if temp == 0:
            return [-1]
        answer.append(temp)
        s -= temp
        n -= 1
    return answer
print(solution(3, 2))