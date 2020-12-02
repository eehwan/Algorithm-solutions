from collections import deque

def isConvertable(a, b):
    return sum(i == j for i,j in zip(a,b)) == len(a) - 1

def solution(begin, target, words):
    if target not in words:
        return 0
    words = {key:0 for key in words}
    words[begin] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        current = queue.popleft()
        for word in words:
            if isConvertable(word, current) and words[word]==0:
                words[word] = words[current] + 1
                queue.append(word)
    return words[target]

print(solution("hit", "hhh", ["hht","hhh", "dod", "dog", "lot", "cog"]))
