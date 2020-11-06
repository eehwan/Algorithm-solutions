n, m = map(int, input().split(" "))
tiles = []
for i in range(n):
    tiles.append(list(map(int, str(input()))))

visited = [[False for _ in range(m)] for _ in range(n)]

count = 1
stacks = []
stacks2 = []
stacks.append([0,0])
while True:
    if stacks == [] and stacks2:
        count+=1
        # print("-----------------------------\n",count)
        stacks, stacks2 = stacks2, []
    # print("\nstacks\n", stacks)
    stack = stacks.pop()
    # print(stack)
    a,b = stack
    if (a, b) == (n-1, m-1):
        break
    if visited[a][b] == True or tiles[a][b] == 0:
        continue
    visited[a][b] = True
    # print("\nvisited\n", visited)
    for aa in  range(a-1,a+2):
        for bb in  range(b-1,b+2):
            if aa < 0 or bb < 0:
                continue
            if aa >= n or bb >= m:
                continue
            if (abs(aa-a), abs(bb-b)) == (1, 1):
                continue
            stacks2.append([aa,bb])
print(count)
