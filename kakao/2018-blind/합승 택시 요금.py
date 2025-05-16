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

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for x, y, fare in fares:
        graph[x].append((y, fare))
        graph[y].append((x, fare))

    dist_from_s = dijkstra(s, n, graph)
    dist_from_a = dijkstra(a, n, graph)
    dist_from_b = dijkstra(b, n, graph)
    
    min_cost = sys.maxsize
    for i in range(1, n + 1):
        min_cost = min(min_cost, dist_from_s[i] + dist_from_a[i] + dist_from_b[i])

    return min_cost


if __name__ == "__main__":
    test_cases = [
        [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],  # 82
        [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],                                                      # 14
        [6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]],                  # 18
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")