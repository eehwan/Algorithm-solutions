from itertools import combinations
def solution(numbers):
    answer = set()
    for a,b in combinations(numbers, 2):
        answer.add(a+b)
    return soterd(list(answer))

print(solution([1,1,1,1,2,3,4,5]))
