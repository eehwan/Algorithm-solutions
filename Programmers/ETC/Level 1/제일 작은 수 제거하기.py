def solution(arr):
    arr.remove(min(arr))
    return len(arr)>2 and arr or [-1]