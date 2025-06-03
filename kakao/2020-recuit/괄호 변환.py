def solution(p):
    def isCorrect(x):
        if (x.startswith("(")):
            cnt = 0
            for i, v in enumerate(x):
                if v == "(":
                    cnt += 1
                else:
                    cnt -= 1

                if cnt < 0:
                    return False
            if cnt == 0:
                return True

        return False
    
    def change(x):
        if x == "":
            return x
        else:
            cnt = 0
            for i, v in enumerate(x):
                if v == "(":
                    cnt += 1
                else:
                    cnt -= 1

                if cnt == 0:
                    a, b = x[:i + 1], x[i + 1:]
                    
                    if isCorrect(a):
                        return a + change(b)
                    else:
                        a = a[1:][:-1].replace("(", ":").replace(")", "(").replace(":", ")")
                        return f'({change(b)}){a}'

    return change(p)

if __name__ == "__main__":
    test_cases = [
        "(()())()",     # "(()())()"
        ")(",           # "()"
        "()))((()",     # "()(())()"
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")