import math

def solution(n, stations, w):
    answer = 0
    start = 0
    for s in stations:
        left = s - w - 1
        right = s + w - 1
        if start < left:
            answer += math.ceil((left - start)/(w*2 + 1))
        start = right + 1
        if start > n:
            return answer
    answer += math.ceil((n - start)/(w*2 + 1))
    return answer

print(solution(11, [4,11], 1))