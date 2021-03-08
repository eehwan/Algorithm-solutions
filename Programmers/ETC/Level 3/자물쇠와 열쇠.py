from copy import deepcopy

def expendArray(array, m, n): # array 가장자리에 각각 m만큼 0 추가
    newArray = array
    for i in range(n):
        newArray[i] = [0 for _ in range(m)] + newArray[i] + [0 for _ in range(m)]
    for _ in range(m):
        newArray.insert(0, [0 for _ in range(n + 2*m)])
        newArray.append([0 for _ in range(n + 2*m)])
    return newArray

def rotateArray(array): # 90도 회전
    length = len(array)
    newArray = []
    for i in range(length):
        temp = []
        for j in range(length):
            temp.append(array[length - 1 -j][i])
        newArray.append(temp)
    return newArray

def isUnlock(key, expendedMap, m, n): # key를 놓을 수 있는 모든 위치를 돌며 체크
    for startX in range(m+n):
        for startY in range(m+n):
            temp = deepcopy(expendedMap)
            for i in range(m):
                for j in range(m):
                    temp[startX+i][startY+j] += key[i][j]
            # print(f"key + expendedMap ({startX}, {startY}):\n{temp}")
            isUnlocked = True
            for i in range(n):
                for j in range(n):
                    if temp[m+i][m+j] != 1:
                        isUnlocked = False
                        break
                if isUnlocked == False:
                    break
            if isUnlocked == True:
                return True
    return False

def solution(key, lock):
    m = len(key)
    n = len(lock)
    rotatedKey = key
    expendedMap = expendArray(lock, m, n)
    for k in range(4):
        rotatedKey = rotateArray(rotatedKey)
        # print(f"rotated: {k}")
        # print("rotatedKey :\n", rotatedKey)
        if isUnlock(rotatedKey, expendedMap, m, n):
            # print("isUnlocked\n",expendedMap)
            return True
    return False