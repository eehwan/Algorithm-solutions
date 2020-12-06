def solution(n):
    triangle = [[0 for _ in range(i+1)] for i in range(n)]
    y, x = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1; x -= 1
            triangle[y][x] = number
            number += 1
    return sum(map(sum, triangle))

print(solution(4))
