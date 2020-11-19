def solution(arrows):
    move = [(0, 1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    current = (0, 0)
    visited_points = {(0,0)}
    visited_path = set()
    for i in arrows:
        for _ in range(2):
            next = tuple(map(sum, zip(current, move[i])))
            visited_path.add(makePath(current, next))
            visited_points.add((next))
            current = next
            print(i,len(visited_path))
    # print("visited_path : ",visited_path)
    return 1 - len(visited_points) + len(visited_path)
def makePath(a, b):
    if a[0] > b[0]:
        answer = f"{a}, {b}"
    elif a[0] == b[0] and a[1] >= b[1]:
        answer = f"{a}, {b}"
    else:
        answer = f"{b}, {a}"
    # print(a,b)
    # print(answer)
    # print()
    return answer


print(solution([6, 2,6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
