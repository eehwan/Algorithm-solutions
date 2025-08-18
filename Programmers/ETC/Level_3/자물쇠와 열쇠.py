from copy import deepcopy

def expendArray(array, keySize, lockSize): # array 가장자리에 각각 keySize만큼 0 추가
    newArray = array
    for i in range(lockSize):
        newArray[i] = [0 for _ in range(keySize-1)] + newArray[i] + [0 for _ in range(keySize-1)]
    for _ in range(keySize-1):
        newArray.insert(0, [0 for _ in range(lockSize + 2*keySize - 2)])
        newArray.append([0 for _ in range(lockSize + 2*keySize - 2)])
    return newArray

def rotateArray(array):
    # 90도 회전

    # length = len(array)
    # newArray = []
    # for i in range(length):
    #     temp = []
    #     for j in range(length):
    #         temp.append(array[length - 1 -j][i])
    #     newArray.append(temp)
    # return newArray

    # -90도 회전
    return list(zip(*array))[::-1]


def isUnlock(key, expendedMap, keySize, lockSize): # key를 놓을 수 있는 모든 위치를 돌며 체크
    for startX in range(keySize-1 + lockSize):
        for startY in range(keySize-1 + lockSize):
            temp = deepcopy(expendedMap)
            for i in range(keySize):
                for j in range(keySize):
                    temp[startX+i][startY+j] += key[i][j]
            # print(f"key + expendedMap ({startX}, {startY}):\n{temp}")
            isUnlocked = True
            for i in range(lockSize):
                for j in range(lockSize):
                    if temp[keySize-1 + i][keySize-1 + j] != 1:
                        isUnlocked = False
                        break
                if isUnlocked == False:
                    break
            if isUnlocked == True:
                return True
    return False

def solution(key, lock):
    keySize = len(key)
    lockSize = len(lock)
    rotatedKey = key
    expendedMap = expendArray(lock, keySize, lockSize)
    for k in range(4):
        rotatedKey = rotateArray(rotatedKey)
        # print(f"rotated: {k}")
        # print("rotatedKey :\n", rotatedKey)
        if isUnlock(rotatedKey, expendedMap, keySize, lockSize):
            # print("isUnlocked\n",expendedMap)
            return True
    return False
    
# numpy를 이용한 풀이

# import numpy as np

# def zip_rotate(original):
#     rotated = np.array(list(zip(*original[::-1])))
#     return rotated

# def solution(key, lock):
#     key = np.array(key)
#     lock = np.array(lock)
#     lock_pad = np.pad(lock,((key.shape[0]-1,key.shape[0]-1),(key.shape[0]-1,key.shape[0]-1)),'constant',constant_values=0)
#     for k in range(4):
#         key = zip_rotate(key)
#         for i in range(0,lock.shape[0]+key.shape[0]-1):
#             for j in range(0,lock.shape[0]+key.shape[0]-1):
#                 lock_pad_copy = lock_pad.copy()
#                 lock_pad_copy[i:(i+key.shape[0]),j:(j+key.shape[0])] = lock_pad[i:(i+key.shape[0]),j:(j+key.shape[0])] + key

#                 lock_main = lock_pad_copy[(key.shape[0]-1):(lock_pad.shape[0]-key.shape[0]+1),(key.shape[0]-1):(lock_pad.shape[0]-key.shape[0]+1)]
#                 lock_main = lock_main==1
#                 if (sum(map(sum,lock_main))==lock.shape[0]**2):
#                     return(True)
#     return(False)