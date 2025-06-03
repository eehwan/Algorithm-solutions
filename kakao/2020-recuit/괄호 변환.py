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
                if cnt == 0 and len(x) - 1 == i:
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
                    if not isCorrect(a):
                        a = "(" + a[1:][:-1].replace("(", ":").replace(")", "(").replace(":", ")") + ")"
                    return a + change(b)

    return change(p)

if __name__ == "__main__":
    test_cases = [
        "(()())()",     # "(()())()"
        ")(",           # "()"
        "()))((()",     # "()(())()"
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")