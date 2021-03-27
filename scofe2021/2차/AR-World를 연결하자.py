# 2번 문제
def solution():
    n = int(input())
    link = []
    visited = {}
    for _ in range(n):
        start, end, cost = input().split(" ")
        cost = int(cost)
        
        link.append([cost, start, end])
        visited[start] = 0
        visited[end] = 0
    link.sort()
    # print(link)
    # print(visited)

    answer = 0
    for current in link:
        if visited[current[1]] == 1 and visited[current[2]] == 1:
            continue
        answer += current[0]
        visited[current[1]] = 1
        visited[current[2]] = 1


    return answer

print(solution())