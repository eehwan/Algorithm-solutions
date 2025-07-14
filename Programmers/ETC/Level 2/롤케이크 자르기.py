def solution(topping):
    answer = -1
    return answer

if __name__ == "__main__":
    test_cases = [
        [1, 2, 1, 3, 1, 4, 1, 2],        # 2
        [1, 2, 3, 1, 4],                 # 0
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")