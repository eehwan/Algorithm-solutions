import math

def solution(r1, r2):
    answer = 0
    for x in range(0, r2 + 1):
        y_max = int(math.sqrt(r2**2 - x**2))
        y_min = int(math.ceil(math.sqrt(r1**2 - x**2))) if x < r1 else 0
        answer += (y_max - y_min + 1)
        if y_min == 0:
            answer -= 1
    return answer * 4


if __name__ == "__main__":
    test_cases = [
        [2, 3],   # 20
        [1, 3],   # 20
        [8, 20],  # 237
        # [1, 100000],  # 237
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")