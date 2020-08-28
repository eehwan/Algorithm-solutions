# def solution(people, limit):
#     people.sort(reverse=True)
#     # print(people, limit)
#     if len(people)<=1:
#         return len(people)
#     weight_in_boat, count_boat = 0, 0
#     i,j = 0,0
#     length = len(people)
#     while i+j< length:
#         weight_in_boat = people[i]
#         i+=1
#         if weight_in_boat + people[-j-1] <= limit:
#             count_boat += 1
#             weight_in_boat = 0
#             j+=1
#         else:
#             count_boat += 1
#             weight_in_boat = 0
#     return count_boat

def solution(people, limit):
    people.sort()
    a, b = 0, len(people)-1
    count = 0
    while a<=b:
        if people[a]+people[b]<=limit:
            a+=1
        b-=1
        count+=1
    return count


test_case =\
"""
[70, 50, 80, 50], 100
[70, 80, 50], 100
[40, 40, 90, 90, 100], 180
[40, 40, 80, 90, 95, 110, 110], 150
"""
expected_value =\
"""
3
3
3
5
"""


print(solution([70, 80, 50], 100))
