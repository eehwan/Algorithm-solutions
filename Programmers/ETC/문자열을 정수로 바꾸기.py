def solution(s):
    if s.startswith("-"):
        return -int(s[1:])
    return int(s)
