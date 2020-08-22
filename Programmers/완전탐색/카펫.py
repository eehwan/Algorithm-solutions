def solution(brown, yellow):
    total = brown+yellow
    for ver in range(2,int(total*0.5)+1):
        if total%ver != 0:
            continue
        hor = total/ver
        if (ver+hor)*2-4 == total-yellow:
            return [hor, ver]
"""
[1, 2, 3, 4, 5]
[1, 3, 2, 4, 2]
"""

"""
[1]
[1,2,3]
"""

print(solution(10,2))
