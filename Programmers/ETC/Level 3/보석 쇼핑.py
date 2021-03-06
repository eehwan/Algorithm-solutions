import heapq
class Gem:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = end  - start
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self , other):
        return self.value > other.value
    def __str__(self):
        return f"[{self.start}, {self.end}]"
    def getList(self):
        return [self.start, self.end]
def solution(gems):
    gemCnt = len(set(gems))
    gemMap = {}
    answer = []
    for i, v in enumerate(gems):
        gemMap[v] = i
        if len(gemMap) == gemCnt:
            temp = gemMap.values()
            heapq.heappush(answer, Gem(min(temp)+1, max(temp)+1))
    return answer[0].getList()