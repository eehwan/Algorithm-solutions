def canImmigrateAll(n, middle, times):
    return sum(middle // time for time in times) >= n
def solution(n, times):
    start, end = 1, max(times) * n
    while start <= end:
        middle = (start + end) // 2
        print(middle)
        if canImmigrateAll(n, middle, times):
            end = middle - 1
        else:
            start = middle + 1
    return start
print(solution(6, [8, 11]))
