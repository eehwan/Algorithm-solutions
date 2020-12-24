def isPrimeNum(k):
    if k < 2:
        return False
    if k == 2 or k == 3:
        return True
    for i in range(2, int(k**0.5 + 2)):
        if k % i == 0:
            return False
    return True
def solution1(n):
    answer = 0
    for i in range(1, n+1):
        if isPrimeNum(i):
            answer += 1
    return answer
    
def solution(n):
    nums = set(range(2, n+1))
    for i in range(2, n+1):
        nums -= set(range(2*i, n+1, i))
    return len(nums)

print(solution(int(input("n :"))))
