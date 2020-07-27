import sys

remain = 1000-int(sys.stdin.readline())

def coinCount(remain):
    count = 0
    if (remain==0):
        return count
    while (remain>=500):
        count+=1
        remain-=500
    while (remain>=100):
        count+=1
        remain-=100
    while (remain>=50):
        count+=1
        remain-=50
    while (remain>=10):
        count+=1
        remain-=10
    while (remain>=5):
        count+=1
        remain-=5
    while (remain>=1):
        count+=1
        remain-=1
    return count
print(coinCount(remain))
