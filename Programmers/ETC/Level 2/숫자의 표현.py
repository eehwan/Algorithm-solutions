from collections import deque
def solution(n):
    answer = 0
    nums = deque()
    for i in range(n, 0, -1):
        nums.append(i)
        if sum(nums) == n:
            answer += 1
            nums.popleft()
        elif sum(nums) > n:
            nums.popleft()
    return answer

def solution1(n):
    return sum(1 for i in range(1, n+1, 2) if n%i == 0)
