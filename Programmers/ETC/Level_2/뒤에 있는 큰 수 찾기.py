def solution(numbers):
    answer = []
    stack = []
    for num in numbers[::-1]:
        while stack and stack[-1] <= num:
            stack.pop()
        answer.append(stack[-1] if stack else -1)
        stack.append(num)
    return answer[::-1]

def solution2(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]

        stack.append(i)

    return result


if __name__ == "__main__":
    def assert_cases(func, cases):
        for i, (args, expected) in enumerate(cases, 1):
            got = func(*args)
            assert got == expected, f"#{i} FAILED: got {got} - expected {expected}"
        print("✅ All PASSED")

    cases = [
        (([2, 3, 3, 5],), [3, 5, 5, -1]),
        (([9, 1, 5, 3, 6, 2],), [-1, 5, 6, 6, -1, -1]),
    ]
    assert_cases(solution, cases)