def solution(s, n):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for l in s:
        if l == " ":
            answer += " "
        else:
            if l.isupper():
                answer += Alphabet[Alphabet.find(l) + n - 26]
            else:
                answer += alphabet[alphabet.find(l) + n - 26]
    return answer

print(solution("zAb", 3))
