from functools import reduce
def greatestCommonDivisor(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
def solution(arr):
    return int(reduce(lambda a,b: a*b/greatestCommonDivisor(a,b), arr))
    
print(solution([1,2,3,5]))
