def solution(n, lost, reserve):
    lost, reserve = set(lost)-set(reserve),set(reserve)-set(lost)
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            continue
        if l+1 in reserve:
            reserve.remove(l+1)
            continue
        n -= 1
    return n



test_case =\
"""
5, [2, 4], [1, 3, 5]
5, [2, 4], [3]
3, [3], [1]
5, [1, 2], [2, 3]
"""
expected_value =\
"""
5
4
2
4
"""


print(solution(5, [1, 2], [2, 3]))
