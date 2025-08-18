def solution(n, words):
    words_list = [words[0]]
    for w in words[1:]:
        if w not in words_list and words_list[-1][-1] == w[0]:
            words_list.append(w)
        else: 
            k = len(words_list) + 1
            a, b = divmod(k, n)
            print(b, a, w, words_list)
            if b == 0:
                return [3, a]
            else:
                return [b, a + 1]
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))