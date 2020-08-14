import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        try:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min1+min2*2)
            count+=1
        except IndexError:
            return -1
    return count



print(solution([1, 2, 3, 9, 10, 12], 7))
