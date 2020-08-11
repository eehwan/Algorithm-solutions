import sys

num = int(sys.stdin.readline())

def fivo(k):
    if(k==0):
        return 0
    elif(k==1):
        return 1
    return fivo(k-2)+fivo(k-1)

print(fivo(num))
