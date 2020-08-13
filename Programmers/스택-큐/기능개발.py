import math
def solution(progresses, speeds):
    complete_day=[]
    for i in range(len(progresses)):
        temp = math.ceil((100-progresses[i])/speeds[i])
        complete_day.append(temp)

    complete_day = [1,3,53,54,7,5,6,4]
    print(complete_day)

    answer = []
    min=complete_day[0]
    count = 0
    for value in complete_day:
        if value <= min:
            count += 1
        else:
            answer.append(count)
            count = 1
            min = value
    answer.append(count)
    return answer

test_case = \
[\
[93, 30, 55], [1, 30, 5]
]
expected_value=\
[\
[2, 1]
]

print(solution([93, 30, 55], [1, 1, 5]))
