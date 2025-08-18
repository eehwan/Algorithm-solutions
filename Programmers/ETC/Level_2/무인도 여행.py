from collections import defaultdict
def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(maps), len(maps[0])
    visited = defaultdict(bool)
    
    def dfs(stack):
        total = 0
        while len(stack) > 0:
            x, y = stack.pop()
            curr = maps[x][y]
            
            total += int(curr)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if visited[nx, ny] != True and maps[nx][ny] != "X":
                        visited[nx, ny] = True
                        stack.append((nx,ny))
            
        return total
                     
    answer = []
    for x in range(rows):
        for y in range(cols):
            if visited[x, y] != True and maps[x][y] != "X":
                visited[x, y] = True
                total = dfs([(x, y)])
                if total != 0:
                    answer.append(total)

    return sorted(answer) or [-1]

test_case = [
    ["X591X", "X1X5X", "X231X", "1XXX1"],   # [1, 1, 27]
    ["XXX", "XXX", "XXX"],                  # [-1]
]

print(*map(solution, test_case))