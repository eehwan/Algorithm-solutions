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
#     def getValue(self):
#         return self.value
#     def getList(self):
#         return [self.start, self.end]
# def solution(gems):
#     typeCnt = len(set(gems))
#     dic = {}
#     answer = BuyList(1, len(gems))
#     for i, v in enumerate(gems):
#         dic[v] = i
#         if len(dic) == typeCnt:
#             temp = dic.values()
#             answer = BuyList(min(temp)+1, max(temp)+1) if answer.getValue() > (max(temp) - min(temp)) else answer
#     return answer.getList()
# # 
# Class를 새로 만들고 비교연산자를 override해서 힙으로 구현했지만
# 힙푸시안에 min, max가 동시에 들어가서 시간 초과가 나는 거 같다.
# 힙대신 value만 비교하여 정답만 저장하는 것도 해보았는데 동작시간이 거의 같았다.

def solution(gems):
    size = len(set(gems))
    dic = { gems[0]: 1 }
    temp = [1, len(gems)]
    start , end = 0, 0
    while(start < len(gems) and end < len(gems)):
        if len(dic) != size:
            end += 1
            if end >= len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if end - start < temp[1] - temp[0]:
                temp = [start + 1, end + 1]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
    return temp

# 최대한 del함수를 쓰지 않고 해결하려고 했었는데 오히려 del을 쓰는게 시간소요가 더 적었다....

test_case = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]

for case in test_case:
    print(solution(case))