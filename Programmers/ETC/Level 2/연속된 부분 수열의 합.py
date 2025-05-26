from collections import deque

def solution(sequence, k):
    left = 0
    total = 0
    answer = [0, len(sequence)]

    for right in range(len(sequence)):
        total += sequence[right]

        while total > k:
            total -= sequence[left]
            left += 1

        if total == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

    return answer

if __name__ == "__main__":
    test_cases = [
        [[1, 2, 3, 4, 5], 7],       # [2, 3]
        [[1, 1, 1, 2, 3, 4, 5], 5], # [6, 6]
        [[2, 2, 2, 2, 2], 6,],      # [0, 2]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")