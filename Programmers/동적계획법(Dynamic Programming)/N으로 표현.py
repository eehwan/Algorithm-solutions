def S(N,coeff):
    num_list=set([int(str(N)*coeff)])
    for i in range(1,coeff):
        for temp1 in S(N,i):
            for temp2 in S(N,coeff-i):
                num_list |= {temp1+temp2,temp1-temp2,temp1*temp2}
                if temp2!=0:
                    num_list |= {temp1//temp2}
    return num_list
def solution(N, number):
    for i in range(1,9):
        if number in S(N,i):
            return i
    return -1


test_case =\
"""
5, 12
5, 31168
"""
expected_value =\
"""
4
-1
"""

print(solution(\
[[-2,-1], [1,2],[-3,0]]\
))
