from collections import Counter

def solution(X, Y):
    counter = Counter(X) & Counter(Y)
    sorted_counter = sorted(counter.elements(), reverse=True)
    
    answer = int("".join(sorted_counter)) if sorted_counter else -1
    return str(answer)

if __name__ == "__main__":
    test_cases = [
        ["100", "2345"],            # "-1"
        ["100", "203045"],          # "0"
        ["100", "123450"],          # "10"
        ["12321", "42531"],         # "321"
        ["5525", "1255"],           # "552"
    ]
    print(*map(lambda x: solution(*x), test_cases), sep="\n")
