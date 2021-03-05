import heapq
class Gem:
    def __init__(self, gemType, num):
        self.gemType = gemType
        self.num = num
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self , other):
        return self.value > other.value
    def __hash__(self):
        return self.num
    def getType(self):
        return self.gemType
    def getNum(self):
        return self.num
    def changeNum(self, num):
        self.num = num
    
def solution(gems):
    typesCount = len(set(gems))
    gemRecord = []
    ans = []
    for i, gemType in enumerate(gems):
        if gemType in map(lambda x: x.getType(), gemRecord):
            gemType = filter(lambda x: x.getNum != i + 1, gemType)
        else:
            heapq.heappush(gemRecord, Gem(gemType, i + 1))
        if len(gemRecord) == typesCount:
            temp = sorted(gemRecord.items(), key = lambda x: x[1])
            ans.append([temp[0][1] + 1, temp[-1][1] + 1])
    return sorted(ans, key = lambda x: x[1]-x[0])[0]