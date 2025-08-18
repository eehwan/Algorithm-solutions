def solution(n):
    answer = ""
    while True:
        if n <= 3:
            answer += "124"[(n%3)-1]
            break
        else:
            q, r = divmod(n-1, 3)
            answer += "124"[r]
            n = q
        print(n, answer)
    return answer[::-1]

# 0이 없는 숫자체계가 굉장히 헷갈린다....
print(solution(13))
