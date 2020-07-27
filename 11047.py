import sys

rep, value = map(int, sys.stdin.readline().split())
list = []
for _ in range(rep):
    list.append(int(sys.stdin.readline()))
list.sort(reverse=True)

def countCoin(x):
    count = 0
    for i in range(rep):
        if(x==0):
            return count
        while (x>=list[i]):
            x-=list[i]
            count+=1
    return count

print(countCoin(value))
