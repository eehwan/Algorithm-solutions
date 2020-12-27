def solution(s):
    answer = 1
    for i in range(0, len(s)):
        for j in range(1, (len(s) - i)//2 + 1):
            if s[i:i+j][::-1] == s[i+j+1: i + 2*j+1]:
                if answer < 2*j + 1: answer = 2*j + 1
            elif s[i:i+j][::-1] == s[i+j: i + 2*j]:
                if answer < 2*j: answer = 2*j
    return answer

print(solution("aa"))
