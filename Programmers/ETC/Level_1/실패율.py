def solution(N, stages):
    defeat_rate = []
    for i in range(1,N+1):
        stop_count = 0
        total_count = 0
        for stage in stages:
            if stage >= i:
                total_count += 1
                if stage == i:
                    stop_count += 1
        if (stop_count, total_count) == (0, 0):
            defeat_rate.append((i,0))
        else:
            defeat_rate.append((i,stop_count/total_count))
    return  [a for a,b in sorted(defeat_rate, key = lambda x: (-x[1],x[0]))]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
