def solution(x, y, n):
    answer = 0
    return answer


if __name__ == "__main__":
    test_cases = [
        [10, 40, 5],    # 2
        [10, 40, 30],   # 1
        [2, 5, 4],      # -1
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
