# import heapq
# class BuyList:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.value = end  - start
#     def __lt__(self, other):
#         return self.value < other.value
#     def __gt__(self , other):
#         return self.value > other.value
#     def __str__(self):
#         return f"[{self.start}, {self.end}]"
#     def getList(self):
#         return [self.start, self.end]
# def solution(gems):
#     typeCnt = len(set(gems))
#     gemMap = {}
#     answer = []
#     for i, v in enumerate(gems):
#         gemMap[v] = i
#         if len(gemMap) == typeCnt:
#             temp = gemMap.values()
#             heapq.heappush(answer, BuyList(min(temp)+1, max(temp)+1))
#     return answer[0].getList()

def solution(gems):
    size = len(set(gems))
    start = 0
    end = len(gems) - 1
    s = set()
    for i in range(len(gems)):
        for j in range(i, len(gems)):
            s.add(gems[j])
            if len(s) == size and end - start > j - i:
                start = i
                end = j
                break
        s.clear()
    return [start + 1, end + 1]
