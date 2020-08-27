def solution(people, limit):
    people.sort()
    weight_in_boat = 0
    count_boat = 0
    for peo in people:
        if weight_in_boat == 0:
            weight_in_boat = peo
        elif weight_in_boat + peo <= limit:
            count_boat += 1
            weight_in_boat = 0
        else:
            count_boat += 1
            weight_in_boat = peo
        print(weight_in_boat, count_boat,limit)
    return count_boat if weight_in_boat==0 else count_boat+1

test_case =\
"""
[70, 50, 80, 50], 100
[70, 80, 50], 100
[40, 40, 90, 90, 100], 180
"""
expected_value =\
"""
3
3
3
"""


print(solution([70, 50, 80, 50], 100))
