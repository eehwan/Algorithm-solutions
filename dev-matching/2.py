import numpy as np
def solution(rows, columns, queries):
    answer = []
    npMap = np.array(list(i for i in range(1, rows*columns+1)))
    npMap = np.reshape(npMap, (columns, rows))
    for x1, y1, x2, y2 in queries:
        npMap[x1-1:x2, y1-1:y2] = moveEdge(np.copy(npMap[x1-1:x2, y1-1:y2]))
        print(npMap)
    return 0
def moveEdge(array):
    # height, width = array.shape()
    # for i in range(height):
    #     for j in range(width):
    #         if i in [0, height-1] or j in [0, width-1]:
    #             tmp = array[i, j]
    return array
       
                
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))