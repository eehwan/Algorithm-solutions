def solution(s):
    queue = []
    for i in s:
        if i == "(":
            queue.append("(")
        else:
            try: queue.pop()
            except: return False
    return len(queue)==0