def solution(arr):
    answer = []
    last_word = ""
    for a in arr:
        if a != last_word:
            answer.append(a)
        last_word = a
    return answer
