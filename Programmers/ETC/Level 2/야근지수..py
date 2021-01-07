import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    while n:
        heapq.heappush(heap, heapq.heappop(heap)+1)
        n -= 1
    return sum(map(lambda x: x**2, heap))

print(solution(1, [4, 5, 3]))