# 재귀를 이용한 풀이
from copy import deepcopy
def solution(k, dungeons, n=0):
    if len(dungeons) == 0: return n
    answers = []
    for i in range(len(dungeons)):
        _dungeons = deepcopy(dungeons)
        x = _dungeons.pop(i)
        require, spend = x
        answers.append(solution(k-spend, _dungeons, n+1 if (k >= require) else n))
    return max(answers)
    
# permutations를 이용한 풀이
from itertools import permutations
def solution(k, dungeons):
    answers = []
    for l in permutations(dungeons, len(dungeons)):
        remain, result = k, 0
        for a,b in l:
            if(remain >= a):
                remain -= b
                result += 1
        answers.append(result)
    return max(answers)