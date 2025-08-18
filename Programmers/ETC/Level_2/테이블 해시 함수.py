from functools import reduce

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    return reduce(
        lambda acc, x: acc ^ x,
        [sum(val % i for val in data[i - 1]) for i in range(row_begin, row_end + 1)],
        0
    )


if __name__ == "__main__":
    test_cases = [
        [[[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3],   # 4
        [[[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3],   # 4
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")