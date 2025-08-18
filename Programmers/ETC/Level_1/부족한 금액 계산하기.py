def solution(price, money, count):
    return max(0, (price * count * (count + 1) // 2) - money)

if __name__ == "__main__":
    test_cases = [
        [3, 20, 4],        # 10
        [5, 20, 4],        # 10
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")