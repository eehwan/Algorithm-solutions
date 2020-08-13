# def solution(priorities, location):
#     new_list = []
#     for i,value in enumerate(priorities):
#         new_list.append([i,value])
#     print(new_list)
#     while new_list != []:
#         priority = new_list[0][1]
#         bool = True
#         for i in range(1,len(new_list)):
#             if new_list[i][1]>priority:
#                 new_list.append(new_list.pop(0))
#                 bool = False
#                 break
#         if bool:
#             print(new_list)
#             answer = new_list.pop(0)
#             print(answer)
#             if answer[0]==location:
#                 return len(priorities)-len(new_list)
def solution(priorities, location):
    length = len(priorities)
    top_priority = max(priorities)
    while True:
        now = priorities.pop(0)
        if now == top_priority:
            if location == 0:
                return length-len(priorities)
            else:
                location-=1
                top_priority = max(priorities)
        else:
            priorities.append(now)
            if location == 0:
                location = len(priorities)-1
            else:
                location-=1

test_case = \
[\
[2, 1, 3, 2], 2
]
expected_value=\
[\
1
]

print(solution(	[2, 1, 3, 2], 2))
