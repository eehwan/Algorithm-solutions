def solution(order):
    temp = []
    answer = 0
    for i in range(1, len(order) + 1):
        if order[answer] == i:
            answer += 1
        else:
            temp.append(i)
        while temp:
            if temp[-1] == order[answer]:
                temp.pop()
                answer += 1
            else:
                break
    return answer


if __name__ == "__main__":
    test_cases = [
        [4, 3, 1, 2, 5],          # 2
        [5, 4, 3, 2, 1],          # 5
        [1, 5, 4, 3, 2],          # 5
        [i for i in range(3000000, 0, -1)],
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")
