from copy import deepcopy
def solution(k, dungeons, n=0):
    if len(dungeons) == 0: return n
    answers = []
    for i in range(len(dungeons)):
        _dungeons = deepcopy(dungeons)
        x = _dungeons.pop(i)
        require, spend = x
        print(k, x, _dungeons, n+1 if (k >= require) else n, sep=" | ")
        answers.append(solution(k-spend, _dungeons, n+1 if (k >= require) else n))
    return max(answers)