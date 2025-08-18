def solution(s):
    answer = []
    for letter in s:
        if answer and answer[-1] == letter:
            answer.pop()
        else:
            answer.append(letter)
    return 1 if not(answer) else 0

print(solution("abcddcba"))
