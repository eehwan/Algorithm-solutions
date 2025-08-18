def solution(a):
    result = [False for _ in a]
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
