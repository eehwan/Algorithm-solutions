from collections import Counter
from itertools import combinations
import math

def solution(orders, course):
    counters = { i: Counter() for i in course }
    for order in orders:
        for i in course:
            menus = combinations(list(order), i)
            for menu in menus:
                counters[i][''.join(sorted(menu))] += 1

    answer = []
    for counter in counters:
        new_list = sorted([(a, b) for a, b in counter.items()], key=lambda x: (-x[1], x[0]))
        curr = -math.inf
        for key, v in new_list:
            if curr <= v and v > 1:
                curr = v
                answer.append(key)
    
    return sorted(answer)


if __name__ == "__main__":
    test_cases = [
        [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]],   # ["AC", "ACDE", "BCFG", "CDE"]
        [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]], # ["ACD", "AD", "ADE", "CD", "XYZ"]
        [["XYZ", "XWY", "WXA"], [2, 3, 4]],                             # ["WX", "XY"]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")