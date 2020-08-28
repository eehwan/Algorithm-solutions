# 왜 집합으로 푸는것은 안되었던 것인가...?
def solution(routes):
    routes.sort()

    sect_list = list()
    for route in routes:
        print(route)
        start, end = route
        if sect_list==[] or sect_list[-1]<start:
            sect_list.append(end)
            print("added",sect_list)
        else:
            sect_list[-1]=min(sect_list[-1],end)
            print("modified",sect_list)
    print(sect_list)
    return len(sect_list)
# def solution(routes):
#     sect_list = list()
#     for route in routes:
#         print(route)
#         start, end = route
#         new_set = set(i for i in range(start,end+1))
#         if all(sect&new_set==set() for sect in sect_list):
#             sect_list.append(new_set)
#             print("added")
#         else:
#             for sect in sect_list:
#                 if sect & new_set != set():
#                     sect &= new_set
#                     print("modified")
#                     break
#     print(sect_list)
#     return len(sect_list)


test_case =\
"""
[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
[[-2,-1], [1,2],[-3,0]]
[[0,0],]
[[0,1], [0,1], [1,2]]
"""
expected_value =\
"""
2
2
1
1
"""

print(solution(\
[[-2,-1], [1,2],[-3,0]]\
))
