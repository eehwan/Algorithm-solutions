import heapq
def solution(jobs):
    total = 0
    heapq.heapify(jobs)
    return jobs



print(solution([[1,0],[0, 3], [1, 9], [2, 6]]))
