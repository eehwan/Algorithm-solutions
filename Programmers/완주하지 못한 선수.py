def solution(participant, completion):
    sort_participant = sorted(participant)
    sort_completion = sorted(completion)
    print(sort_participant,sort_completion)
    for  index,value in enumerate(sort_participant):
        try:
            print(f"{value} - {sort_completion[index]}")
            if value != sort_completion[index]:
                return value
        except:
            return sort_participant[-1]

test_case =\
"""
["leo", "kiki", "eden"],["eden", "kiki"]
["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]
["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
"""
expected_value =\
"""
leo, vinko,	mislav
"""


print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
