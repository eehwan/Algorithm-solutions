import sys

rep = int(sys.stdin.readline())

for _ in range(rep):
    ppl = int(sys.stdin.readline())
    scores = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(ppl)],key= lambda x:x[0])
    # print("========================================")
    # print(scores)
    count = 0
    aMax = 100001
    bMax = 100001
    for score in scores:
        if (score[0] > aMax and score[1] > bMax):
            print("exeception")
            continue
        if score[0] < aMax:
            aMax = score[0]
        if score[1] < bMax:
            bMax = score[1]
        # print(score,aMax,bMax,"\n","counted",scores.index(score),"th")
        count+=1
    print(count)
