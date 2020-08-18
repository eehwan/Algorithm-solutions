from functools import reduce
def new_sort(num):
    ans = ""
    for i in range(4):
        if i<len(num):
            ans+=num[i]
        else:
            ans+=num[0]
    return ans
def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    print(list(map(new_sort,numbers)))
    print("__________________________")
    numbers.sort(key =lambda x: (new_sort(x),len(x)), reverse=True)
    print(numbers)
    print(list(map(new_sort,numbers)))
    return str(int(reduce(lambda x,y:x+y, numbers,"")))

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key =lambda x: x*3, reverse=True)
#     return str(int("".join(numbers)))

# from itertools import permutations as permut
# def solution2(numbers):
#     numbers = list(map(str, numbers))
#     array = []
#     for x in permut(numbers, len(numbers)):
#         array.append("".join(x))
#     return max(array)
"""
[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
"""

"""
[5,6,3]
"""
print(solution([0,0]))
print(solution([96,966,9699,9696,69,6969,699,6966,6999]))
print(solution2([96,966,9699,9696,69,6969,699,6966,6999]))
