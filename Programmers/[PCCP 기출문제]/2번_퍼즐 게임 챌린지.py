def solution(diffs, times, limit):
    def calc_time(level):
        print(level)
        time_spent = 0
        for i in range(len(diffs)):
            diff, time, prev_time = diffs[i], times[i], 0 if i==0 else times[i-1]

            time_spent += max(diff - level, 0) * (prev_time + time) + time
            print(i, time_spent)
        print(f'time_spent {time_spent}')
        return time_spent

    time_spent, low, high = 0, 1, max(diffs)
    print(f'''\
          diffs {diffs}\
          times {times}\
          limit {limit}\
          ''')
    while high != low:
        print(low, '~', high)
        level = int((low + high) / 2)
        time_spent = calc_time(level)
        if (time_spent > limit):
            low = level + 1
        else:
            high = level
        time_spent = 0

    return high

test_cases = [
    [[1, 5, 3], [2, 4, 7], 30],
    [[1, 4, 4, 2], [6, 3, 8, 2], 59],
    # [[1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723],
    # [[1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012],
]
for x in test_cases:
    print(solution(x[0], x[1], x[2]))