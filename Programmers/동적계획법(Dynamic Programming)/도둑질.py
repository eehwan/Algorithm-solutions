def solution(money):
    f_dp = [money[0], money[0]]
    s_dp = [0, money[1]]
    for i in range(2,len(money)-1):
        f_dp.append(max(f_dp[i-2]+ money[i], f_dp[i-1]))
    for i in range(2,len(money)):
        s_dp.append(max(s_dp[i-2]+ money[i], s_dp[i-1]))
    return max(f_dp[-1], s_dp[-1])
