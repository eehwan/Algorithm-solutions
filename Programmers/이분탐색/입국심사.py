def solution(n, times):
    times.sort(reverse = True)
    queue = [0 for _ in range(len(times))]
    for _ in range(n):
        for j in range(len(queue)):
            if j == len(queue)-1 or (queue[j] + 1)* times[j] < (queue[j+1] + 1) * times[j+1]:
                queue[j] += 1
                break
    print(queue, times)
    return max(a*b for a,b in zip(queue, times))
print(solution(6, [7, 10]))
