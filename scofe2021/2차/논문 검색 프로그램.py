# 4번 문제
a  = int(input())
indexList = []
for _ in range(a):
    indexList.append(input())
# print(indexList)

b = int(input())
for _ in range(b):
    findingWord = input()
    indexCnt = 0
    for index in indexList:
        if index.find(findingWord) >= 0:
            indexCnt += 1
    # print(findingWord)
    print(indexCnt)