from collections import deque

def getGroups(n, wires):    
    graph = { i : set() for i in range(1, n+1) }
    
    for x, y in wires:
        graph[x].add(y)
        graph[y].add(x)
    
    visited = set()
    groupCntList = []
    for point in graph:
        while point not in visited:
            queue = deque([point])
            group = set()
            
            while queue:
                nextPoint = queue.popleft()
                if nextPoint not in visited:
                    visited.add(nextPoint)
                    group.add(nextPoint)
                    queue.extend(graph[nextPoint] - visited)
            
            groupCntList.append(len(group))

    return groupCntList

def solution(n, wires):
    answers = []
    for i in range(n-1):
        newWires = [v for idx, v in enumerate(wires) if idx != i]
        cntList = getGroups(n, newWires)

        answers.append(abs(2 * max(cntList) - n))
    
    return min(answers)

solution(12, [[1, 5], [2, 5], [3, 6], [3, 7], [3, 12], [4, 5], [4, 7], [4, 10], [8, 9], [9, 10], [11, 12]])