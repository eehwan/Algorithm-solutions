import sys

x, y = map(int, sys.stdin.readline().split())
A = []
B = []

for i in range(x):
    A.append(list(str(input())))
for i in range(x):
    B.append(list(str(input())))
print(" A : ",A)
print(" B : ",B)
