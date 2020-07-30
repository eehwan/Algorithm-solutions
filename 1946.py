import sys

rep = int(sys.stdin.readline())


for _ in range(rep):
    scores =[]
    ppl = int(sys.stdin.readline())
    for _ in range(ppl):
        scores.append(list(map(int, sys.stdin.readline().split())))

    scores.sort(key=lambda x:x[0])
    print(scores)
    for score_1 in scores:
        print(score_1)
        for score_2 in scores[scores.index(score_1)+1:]:
            print("score_1, score_2",score_1,score_2)
            if score_1[1] < score_2[1]:
                print("deleted : {}".format(score_2))
                scores.remove(score_2)
    print(len(scores))
