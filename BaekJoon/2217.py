import sys

num = int(sys.stdin.readline())
ropes = []
for i in range(num):
    ropes.append(int(sys.stdin.readline()))
ropes.sort(reverse=True)

def ropeMax(ropeList):
    max = 0
    for rope in ropeList:
        if (rope*(ropeList.index(rope)+1) > max):
            max =  rope*(ropeList.index(rope)+1)
    return max
print(ropes)
print(ropeMax(ropes))
