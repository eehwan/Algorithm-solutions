def solution(n,a,b):
    iter = 0
    while a != b:
        iter += 1
        a, b = (a+1)//2, (b+1)//2
    return iter