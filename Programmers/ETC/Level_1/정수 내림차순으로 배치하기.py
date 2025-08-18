from functools import reduce
def solution(n):
    return int(reduce(lambda a,b: str(a)+str(b), sorted(list(str(n)),reverse=True)))
