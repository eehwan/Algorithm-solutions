from collections import Counter

def solution(topping):
    answer = 0

    left, right = Counter(), Counter(topping)
    left_types, right_types = 0,  len(right)

    for t in topping:
        if left[t] == 0:
            left_types += 1
        left[t] += 1

        right[t] -= 1
        if right[t] == 0:
            right_types -= 1

        if left_types == right_types:
            answer += 1

    return answer

if __name__ == "__main__":
    test_cases = [
        [1, 2, 1, 3, 1, 4, 1, 2],        # 2
        [1, 2, 3, 1, 4],                 # 0
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")