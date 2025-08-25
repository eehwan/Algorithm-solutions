def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        x, y = divmod(i, n)
        if (y <= x):
            answer.append(x + 1)
        else:
            answer.append(y + 1)
    return answer


if __name__ == "__main__":
    def assert_cases(func, cases):
        for i, (args, expected) in enumerate(cases, 1):
            got = func(*args)
            assert got == expected, f"#{i} FAILED: got {got} - expected {expected}"
        print("✅ All PASSED")

    cases = [
        ((3, 2, 5),  [3, 2, 2, 3]),
        ((4, 7, 14), [4, 3, 3, 3, 4, 4, 4, 4]),
    ]
    assert_cases(solution, cases)