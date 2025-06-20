def solution(elements):
    result = set()
    for i in range(1, len(elements) + 1):
        temp = elements + elements
        for j in range(len(elements)):
            result.add(sum(temp[j: j + i]))
    return len(result)


if __name__ == "__main__":
    test_cases = [
        [7, 9, 1, 1, 4],   # 18
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")