from math import comb

def solution(n):
    bin_n = format(n, "b")
    LEN, CNT = len(bin_n), bin_n.count("1")
    answer = 0

    for i, char in enumerate(bin_n):
        if (char == "0"): continue
        if 0 <= CNT <= (LEN - i -1):
            answer += comb(LEN - i -1, CNT)
        CNT -= 1
        if CNT < 0: break

    return answer