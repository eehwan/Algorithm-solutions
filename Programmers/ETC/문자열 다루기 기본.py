def solution(s):
    if len(s) != 4 and len(s) !=6:
        return False
    for i in s:
        try:
            int(i)
        except:
            return False
    return True

def solution2(s):
    return s.isdecimal() and len(s) in (4,6)
