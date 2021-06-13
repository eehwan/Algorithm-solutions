# def solution(arr1, arr2):
#     answer = []
#     for arr11, arr22 in zip(arr1, arr2):
#         temp = []
#         for arr111, arr222 in zip(arr11, arr22):
#             temp.append(arr111+arr222)
#         answer.append(temp)
#         temp = []
#     return answer
def solution(arr1, arr2):
    return [[arr111+arr222 for arr111, arr222 in zip(arr11, arr22)] for arr11,arr22 in zip(arr1, arr2)]