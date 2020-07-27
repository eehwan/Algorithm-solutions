import sys

rep = int(input())

def bigNum(a,b):
    return a>b and a or b
def smallNum(a,b):
    return a<b and a or b


def numOfPoint():
    userInput = sys.stdin.readline()
    (x1, y1, r1, x2, y2, r2) = map(int, userInput.split())
    d = (x1-x2)**2 + (y1-y2)**2
    r = (r1+r2)**2

    if (x1==x2 and y1==y2):
        if (r1==r2):
            return -1
        else:
            return 0
    elif(d == r):          #외접
        return 1
    elif (d < r):          #가까워짐
        if(d**0.5+smallNum(r1,r2)>bigNum(r1,r2)):          #내접 전까지
            return 2
        elif(d**0.5+smallNum(r1,r2)==bigNum(r1,r2)):       # 내접
            return 1
        else:                                              # 전체가 원 안
            return 0
    return 0

for _ in range(rep):
    print(numOfPoint())
