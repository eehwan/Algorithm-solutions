def solution(distance, rocks, n):
    rocks.sort()
    start, end = 1, distance
    while start <= end:
        middle = (start + end) // 2
        pre_rock = 0
        count_rock = 0
        mins = float('inf')
        for rock in rocks:
            if middle > rock - pre_rock:
                count_rock += 1
            else:
                mins = min(mins, rock - pre_rock)
                pre_rock = rock
        if count_rock > n:
            end = middle - 1
        else:
            answer = mins
            start = middle + 1
    return answer

print(solution(26, [2, 5, 14, 17, 23, 24], 3))
