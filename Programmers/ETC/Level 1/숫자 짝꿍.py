def solution(X, Y):
    answer = ''
    return answer


if __name__ == "__main__":
    test_cases = [
        ["100", "2345"],            # "-1"
        ["100", "203045"],          # "0"
        ["100", "123450"],          # "10"
        ["12321", "42531"],         # "321"
        ["5525", "1255"],           # "552"
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
