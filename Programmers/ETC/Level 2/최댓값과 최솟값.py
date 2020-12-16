def solution(s):
    answer = sorted(map(int, s.split(" ")))
    return f'{answer[0]} {answer[-1]}'
