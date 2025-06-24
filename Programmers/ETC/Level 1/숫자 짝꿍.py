from collections import Counter

def solution(X, Y):
    counter = Counter(X) & Counter(Y)
    
    result = []
    for char in map(str, range(9, -1, -1)):
        count = counter[char]
        if (count > 0):
            result.append(char * count)

    answer = "".join(result)
    if answer == "":
        answer = "-1"
    if answer[0] == "0":
        answer = "0"
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
