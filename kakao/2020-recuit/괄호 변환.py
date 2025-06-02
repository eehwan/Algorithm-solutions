def solution(p):
    answer = 0
    return answer

if __name__ == "__main__":
    test_cases = [
        "(()())()",     # "(()())()"
        ")(",           # "()"
        "()))((()",     # "()(())()"
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")