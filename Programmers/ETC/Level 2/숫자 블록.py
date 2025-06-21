def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
        else:
            limit = min(10000000, i // 2, int(i ** 0.5))
            temp = [1]
            for j in range(limit, 1, -1):
                if i % j == 0:
                    temp += filter(lambda x: x <= 10000000, [j, i // j])
            result.append(max(temp))
    return result


if __name__ == "__main__":
    test_cases = [
        [1, 10],                    # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
        [477559014, 477559014],     # [6]
        [1000000000, 1000000000],   # [10000000]
        [100000007, 100000007],     # [1]
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
