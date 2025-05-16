from functools import reduce
from collections import defaultdict
import heapq
import sys

def dijkstra(start, n, graph):
    distances = [sys.maxsize] * (n + 1)
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        if current_dist > distances[current_node]:
            continue
        
        for adjacent, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    
    return distances

def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    costs = dijkstra(1, N, graph)
    print(costs)

    return reduce(lambda acc, x: acc + (1 if x <= K else 0), costs, 0)

if __name__ == "__main__":
    test_cases = [
        [6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4],
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")