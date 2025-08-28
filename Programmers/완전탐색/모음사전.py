import itertools

def solution(word):
    word_list = []
    char_list = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        word_list.extend(map(lambda x: "".join(x), itertools.product(char_list, repeat=i)))
        
    return sorted(word_list).index(word) + 1

if __name__ == "__main__":
    def assert_cases(func, cases):
        for i, (args, expected) in enumerate(cases, 1):
            got = func(*args)
            assert got == expected, f"#{i} FAILED: got {got} - expected {expected}"
        print("✅ All PASSED")

    cases = [
        (("AAAAE",),  6),
        (("AAAE",), 10),
        (("I",), 1563),
        (("EIO",), 1189),
    ]
    assert_cases(solution, cases)