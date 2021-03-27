# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
m, n = map(int, input().split(" "))
market = [[0 for _ in range(m+1)]]
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(n):
	temp = list(map(int, input().split(" ")))
	temp.insert(0, 0)
	market.append(temp)
	
for i in range(1, m+1):
	for j in range(1, n+1):
		if visited[j][i] == 1:
			continue
		market[j][i] += max(market[j-1][i], market[j][i-1])
		visited[j][i] = 1
print(market[-1][-1])