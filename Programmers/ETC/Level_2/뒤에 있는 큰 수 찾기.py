def solution(numbers):
    answer = []
    queue = []
    for num in numbers[::-1]:
        curr = -1
        while queue:
            _curr = queue.pop()
            if num < _curr:
                queue.append(_curr)
                curr = _curr
                break
        queue.append(num)
        answer.append(curr)
    return answer[::-1]

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