def solution(number, k):
    stack = [number[0]]
    for num in list(number)[1:]:
        print(num,stack)
        while len(stack)>0 and stack[-1]<num and k>0:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack) if k==0 else "".join(stack)[:-k]

test_case =\
"""
"1924", 2
"1231234", 3
"4177252841", 4
"123917415", 6
"12398745", 5
"""
expected_value =\
"""
94
"3234"
"775841"
"975"
"987"
"""


print(solution("12398745", 5))
