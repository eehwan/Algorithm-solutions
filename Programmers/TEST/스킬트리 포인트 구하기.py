def solution(total_sp, skills):
    child_map, parent_map, point_map = {}, {}, {}
    for i in range(len(skills) + 1):
        child_map[str(i+1)] = []
        parent_map[str(i+1)] = []
    for skill in skills:
        a, b = map(str, skill)
        child_map[a].append(b)
        parent_map[b].append(a)

    def dfs(n):
        if len(child_map[n]) == 0:
            point_map[n] = 1
            return 1
        result = 0
        for child in child_map[n]:
            result += dfs(child)
        point_map[n] = result
        return result

    dfs(*filter(lambda x: len(parent_map[x]) == 0, parent_map))

    multiple = total_sp / sum(point_map.values())
    answer = list(map(lambda x: multiple * x, [point_map[k] for k in sorted(point_map)]))
    # print(point_map, sum(point_map.values()))
    return answer

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