def solution(n,  From=1, Toward=3, Sub=2):
    if n == 1:
        return([[From, Toward]])
    return solution(n - 1, From, Sub, Toward) + [[From, Toward]] + solution(n - 1, Sub, Toward, From)

def solution1(n):
    def hanoi(n, From, Toward, Sub):
        if n == 1:
            answer.append([From, Toward])
            return
        hanoi(n - 1, From, Sub, Toward)
        answer.append([From, Toward])
        hanoi(n - 1, Sub, Toward, From)
    
    answer = []
    hanoi(n, 1, 3, 2)
    return answer

def solution2(n):
    def hanoi(n,  From=1, Toward=3, Sub=2):
        if n == 1:
            yield([From, Toward])
        yield from solution(n - 1, From, Sub, Toward)
        yield [From, Toward]
        yield from solution(n - 1, Sub, Toward, From)
    return [x for x in hanoi(5)]

print(solution2(5))