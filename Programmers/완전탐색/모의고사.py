def solution(answers):
    answer = []
    people = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for person in people:
        length=len(person)
        count=0
        for i,value in enumerate(answers):
            if value==person[i%length]:
                count += 1
        answer.append(count)
    max_answer = max(answer)
    result = []
    for i,value in enumerate(answer):
        if value == max_answer:
            result.append(i+1)
    return result

"""
[1, 2, 3, 4, 5]
[1, 3, 2, 4, 2]
"""

"""
[1]
[1,2,3]
"""

print(solution([1, 3, 2, 4, 2]))
