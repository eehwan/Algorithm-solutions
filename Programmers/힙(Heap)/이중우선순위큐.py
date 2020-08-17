def solution(operations):
    deque = []
    for op in operations:
        x,y = op.split(" ")
        if x == "D":
            y = int(y)
            try:
                if y == 1:
                    deque.pop()
                else:
                    deque.pop(0)
            except IndexError:
                pass
        else:
            deque.append(int(y))
            deque.sort()
    return [deque[-1],deque[0]] if deque else [0,0]

"""
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
"""

"""
[0,0]
[333, -45]
"""

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
