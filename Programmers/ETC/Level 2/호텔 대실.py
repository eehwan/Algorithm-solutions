import heapq

def solution(book_time):
    book_time.sort()
    answer = 0
    heap = []

    for v in book_time:
        start_time, end_time = [
            int(h) * 60 + int(m) + 10
            for h, m in (x.split(":") for x in v)
        ]
        while heap and heap[0] <= start_time:
            heapq.heappop(heap)
        heapq.heappush(heap, end_time + 10)
        answer = max(len(heap), answer)
        
    return answer

if __name__ == "__main__":
    test_cases = [
        [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]],                       # 3
        [["09:10", "10:10"], ["10:20", "12:20"]],                                                                                   # 1
        [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]],                                                               # 3
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")