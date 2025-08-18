import sys
def solution(n):
    for x in range(n+1, sys.maxsize):
        if bin(x).count("1") == bin(n).count("1"):
            return x 

print(solution(78))