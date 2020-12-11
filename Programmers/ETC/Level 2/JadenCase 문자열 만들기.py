def solution(s):
    return " ".join(map(lambda x: x[0].upper() + x[1:].lower() if x else "", s.split(" ")))

print(solution(""))
