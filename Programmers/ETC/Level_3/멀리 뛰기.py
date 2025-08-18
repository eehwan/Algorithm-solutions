def solution(n):
    dp = [0, 1, 2]
    if n <= 2:
        return dp[n]
    for i in range(3, n+1):
        dp.append(dp[i-2] + dp[i-1])
    return dp[-1]%1234567
# 이론적으로는 둘이 같아야 하지만 int값 오류때문에 77부터 다름
def solution2(n):
    maxNumOf2 = n//2
    count = 0
    for numOf2 in range(maxNumOf2+1):
        numOf1 = n - (2*numOf2)
        temp = 1
        for j in range(1,numOf2+1):
            temp *= (numOf1+j)/j
        count += int(temp)
    return int(count)%1234567

print(solution(77), solution2(77))
for i in range(77,79):
    if solution(i) != solution2(i):
        print(i, solution(i), solution2(i))
