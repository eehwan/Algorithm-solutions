# 3번 문제
numProd, numLine = map(int, input().split(" "))
map = {str(n):[] for n in range(1, numProd + 1)}
for _ in range(numProd - 1):
    up, down = input().split(" ")
    # print(up, down)
    map[up].append(down)
    # print("---------------------------")
# print(map)
def solution(up, down):
    queue = [up]
    while queue:
        current = queue.pop()
        # print("current :", current)
        if current == down:
            return True
        queue += map[current]
    return False

# 출력문
for _ in range(numLine):
    up, down = input().split(" ")
    answer = "yes" if solution(up, down) else "no"
    print(answer)
