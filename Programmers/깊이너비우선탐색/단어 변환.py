def func(word1, word2):
    match_num = 0
    for a,b in zip(word1, word2):
        if a == b:
            match_num += 1
    print("func\n", word1, word2, match_num)
    return match_num
def solution(begin, target, words, count = 0):
    print("=======================================")
    print("start\n", begin, target, words, count)
    if target not in words:
        return 0
    if func(begin, target) == len(target) - 1:
        return count + 1
    for next_begin in words:
        print("\nchechking words:\n", begin, next_begin, "\n")
        if func(begin, next_begin) == 2 and func(next_begin, target) > func(begin, target):
                print(next_begin, words[1:], count+1)
                return solution(next_begin, target, words[1:], count+1)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
