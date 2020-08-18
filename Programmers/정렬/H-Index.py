def solution(citations):
    citations.sort(reverse=True)
    ans = []
    for i,value in enumerate(citations):
        ans.append(min(i+1,value))
    return max(ans)

# def solution(citations):
#     return max(list(min(i+1,value) for i,value in enumerate(sorted(citations,reverse=True))))

# def solution(citations):
#     citations.sort()
#     length = len(citations)
#     for i,value in enumerate(citations):
#         if value>=length-i:
#             return length-i
#     return 0

"""
[3, 0, 6, 1, 5]
[2,4,33,65]
[65,55]
"""

"""
3
3
2
"""
print(solution([65,55]))
