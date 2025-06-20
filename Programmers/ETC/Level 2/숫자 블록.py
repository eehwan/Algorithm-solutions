def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
        else:
            v = 1
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    v = i // j
            result.append(v)
    return result


if __name__ == "__main__":
    test_cases = [
        [1, 10],   # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
