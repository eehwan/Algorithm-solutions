import math

def solution(n, stations, w):
    answer = 0
    start = 0
    for i in range(len(stations)):
        left = stations[i] - w - 1
        right = stations[i] + w - 1
        if start >= left and start <= right:
            start = right + 1
            continue
        answer += math.ceil((left - start) / (w * 2 + 1))        
        start = right + 1
    
    if start < n:
        answer += math.ceil((n - start) / (w * 2 + 1))
    
    return answer

print(solution(11, [4,11], 1))