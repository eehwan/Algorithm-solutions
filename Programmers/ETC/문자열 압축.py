def solution(s):
    if len(s)==1: return 1
    words = []
    for i in range(1, int(len(s)//2)+1):
        new_word = ""
        word_count = 1
        temp_word = s[:i]
        for j in range(i, len(s)+1, i):
            if s.startswith(temp_word, j):
                word_count += 1
            else:
                if word_count != 1:
                    new_word += str(word_count)
                new_word += temp_word

                word_count = 1
                temp_word = s[j:j+i]
        if len(s)%i:
            new_word += s[-(len(s)%i):]
        words.append(new_word)
    return min(map(len, words))

print(solution("abcabcabcabcdededededede"))
