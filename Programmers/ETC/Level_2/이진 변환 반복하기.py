def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[0] += 1
        answer[1] += s.count("0")
        s = format(s.count("1"), "b")
    return answer
print(solution("110010101001")) 