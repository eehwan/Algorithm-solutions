def solution(s, n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ""
    for l in s:
        if l == " ":
            answer += " "
        else:
            if l.isupper():
                print(alphabet.find(l)-26+n)
                answer += alphabet[alphabet.find(l) + n - 26]
            else:
                answer += alphabet[alphabet.find(l.upper()) + n - 26].lower()
    return answer

print(solution("z", 1))
