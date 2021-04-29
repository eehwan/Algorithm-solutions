import numpy as np
def solution(rows, columns, queries):
    answer = []
    npMap = np.array(list(i for i in range(1, rows*columns+1)))
    npMap = np.reshape(npMap, (columns, rows))
    for x1, y1, x2, y2 in queries:
        npMap[x1-1:x2, y1-1:y2], tmp = moveEdge(np.copy(npMap[x1-1:x2, y1-1:y2]))
        answer.append(int(tmp))
    return answer
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def moveEdge(array):
    height, width = list(array.shape)
    newArray = np.copy(array)
    MIN = float('inf')
    for i in range(height):
        for j in range(width):
            if i == 0 and j in range(0, width-1):
                di, dj = moves[0][0] + i, moves[0][1] + j
                newArray[di, dj] = array[i, j]
                MIN = min(newArray[di, dj], MIN)
            if i in range(0, height-1) and j == width-1:
                di, dj = moves[1][0] + i, moves[1][1] + j
                newArray[di, dj] = array[i, j]
                MIN = min(newArray[di, dj], MIN)
            if i == height-1 and j in range(1, width):
                di, dj = moves[2][0] + i, moves[2][1] + j
                newArray[di, dj] = array[i, j]
                MIN = min(newArray[di, dj], MIN)
            if i in range(1, height) and j == 0:
                di, dj = moves[3][0] + i, moves[3][1] + j
                newArray[di, dj] = array[i, j]
                MIN = min(newArray[di, dj], MIN)
    # print(array, newArray)
    return [newArray, MIN]
       
                
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))