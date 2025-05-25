from collections import deque

def solution(sequence, k):
    total = 0
    queue = deque()
    index = [0, len(sequence)]
    answer = [0, len(sequence)]
    for i, value in enumerate(sequence):
        if (total <= k):
            total += value
            index[1] = i
            queue.append(value)
        while (total > k):
            index[0] += 1
            x = queue.popleft()
            total -= x
        if total == k:
            if index[1] - index[0] < answer[1] - answer[0]:
                answer = [index[0], index[1]]
    return answer

if __name__ == "__main__":
    test_cases = [
        [[1, 2, 3, 4, 5], 7],       # [2, 3]
        [[1, 1, 1, 2, 3, 4, 5], 5], # [6, 6]
        [[2, 2, 2, 2, 2], 6,],      # [0, 2]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")