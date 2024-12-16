def solution(diffs, times, limit):
    def calc_time(level):
        time_spent = sum(
            max(diff - level, 0) * (0 if i == 0 else times[i - 1] + time) + time
            for i, (diff, time) in enumerate(zip(diffs, times))
        )
        return time_spent

    low, high = 1, max(diffs)
    while high != low:
        level = (low + high) >> 1
        time_spent = calc_time(level)
        if time_spent > limit:
            low = level + 1
        else:
            high = level
    return high

# test_cases = [
#     [[1, 5, 3], [2, 4, 7], 30],
#     [[1, 4, 4, 2], [6, 3, 8, 2], 59],
#     [[1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723],
#     [[1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012],
# ]
# for x in test_cases:
#     print(solution(x[0], x[1], x[2]))