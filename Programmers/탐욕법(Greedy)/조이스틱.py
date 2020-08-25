def alphb_change(alp):
    alphb_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    index = alphb_list.index(alp)
    return min(index,-index+len(alphb_list))
def solution(name):
    count_list = list(map(alphb_change,list(name)))
    answer = 0
    index = 0
    while sum(count_list)!=0:
        for i,v in enumerate(count_list):
            if v!=0:
                from_front = i
                break
        for i,v in enumerate(count_list[::-1]):
            if v!=0:
                from_back = -i-1
                break
        if from_front-index<=-from_back+index:
            answer += from_front-index
            index = from_front
            # print("앞")
        else:
            answer += -from_back+index
            index = from_back
            # print("뒤")
        # print(index,answer)
        answer += count_list[index]
        # print(index,answer,"\n")
        count_list[index] = 0
    return answer

test_case =\
"""
"JEROEN"
"JAN"
"JAGAAAN"
"""
expected_value =\
"""
56
"987"
"32"
"""


print(solution("JAGAAAN"))
