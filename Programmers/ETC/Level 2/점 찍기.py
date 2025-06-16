import math

def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        answer += int(math.sqrt(d**2 - x**2))//k + 1
    return answer


if __name__ == "__main__":
    test_cases = [
        [2, 4],   # 6
        [1, 5],   # 26
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")