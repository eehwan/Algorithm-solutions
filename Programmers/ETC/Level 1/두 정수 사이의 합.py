from functools import reduce
def solution(a, b):
    return reduce(lambda x,y: x+y, range(a,b+1) if a<b else range(b,a+1))
