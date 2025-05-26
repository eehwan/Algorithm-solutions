def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    answer = 0
    for i in range(row_begin, row_end + 1):
        answer ^= sum(x % i for x in data[i - 1])
    
    return answer


if __name__ == "__main__":
    test_cases = [
        [[[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3],   # 4
        [[[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3],   # 4
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")