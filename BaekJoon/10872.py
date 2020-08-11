import sys

num = int(sys.stdin.readline())

def factorial(k):
    if (k==0):
        return 1
    return k*factorial(k-1)

print(factorial(num))
