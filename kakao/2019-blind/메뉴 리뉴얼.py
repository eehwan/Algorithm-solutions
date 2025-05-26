from collections import Counter
from itertools import combinations

def solution(orders, course):
    counters = { i: Counter() for i in course }
    for order in orders:
        for i in course:
            for menu in combinations(sorted(list(order)), i):
                counters[i][''.join(menu)] += 1

    answer = []
    for counter in counters.values():
        if not counter:
            continue
        max_count = max(counter.values())
        if max_count < 2:
            continue
        for key, v in counter.items():
            if v == max_count:
                answer.append(key)
    
    return sorted(answer)


if __name__ == "__main__":
    test_cases = [
        [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]],   # ["AC", "ACDE", "BCFG", "CDE"]
        [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]], # ["ACD", "AD", "ADE", "CD", "XYZ"]
        [["XYZ", "XWY", "WXA"], [2, 3, 4]],                             # ["WX", "XY"]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")