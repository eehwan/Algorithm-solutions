from itertools import permutations as permut
def isPrimeNum(num):
    if num<2 or num==4:
        return False
    for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
            return False
    return True
def makeSet(numbers):
    num_set = set()
    for i in range(1,len(numbers)+1):
        for p in permut(list(numbers),i):
            num_set.add(int("".join(p)))
    return num_set
def solution(numbers):
    return sum(list(isPrimeNum(n) for n in makeSet(numbers)))

""" ## 에라토스테네스 체
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
"""

"""
"17"
"011"
"""

"""
3
2
"""

print(solution("17"))
