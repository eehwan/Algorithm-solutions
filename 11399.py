import sys

rep = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
nums = list(map(int,nums))

def smallest(x:list):
    x.sort()
    return x.pop(0)

total = 0
sum = 0
for _ in range(rep):
    sum += smallest(nums)
    total += sum
print(total)
