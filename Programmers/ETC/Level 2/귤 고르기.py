def solution(k, tangerine):
    answer = 0
    return answer

if __name__ == "__main__":
    test_cases = [
        [6, [1, 3, 2, 5, 4, 5, 2, 3]],  # 3
        [4, [1, 3, 2, 5, 4, 5, 2, 3]],  # 3
        [2, [1, 1, 1, 1, 2, 2, 2, 3]],  # 1
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")