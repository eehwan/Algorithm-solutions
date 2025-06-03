def solution(p):
    def is_correct(x):
        cnt = 0
        for char in x:
            if char == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                break
        return cnt == 0
    
    def transform(s):
        if not s:
            return ""
        
        cnt = 0
        for i, char in enumerate(s):
            if char == "(":
                cnt += 1
            else:
                cnt -= 1
        
            if cnt == 0:
                u, v = s[:i + 1], s[i + 1:]
                
                if is_correct(u):
                    return u + transform(v)
                else:
                    new_u = ''.join(')' if c == '(' else '(' for c in u[1:-1])
                    return '(' + transform(v) + ')' + new_u

    return transform(p)

if __name__ == "__main__":
    test_cases = [
        "(()())()",     # "(()())()"
        ")(",           # "()"
        "()))((()",     # "()(())()"
    ]
    print(*map(lambda x: solution(x), test_cases), sep="\n")