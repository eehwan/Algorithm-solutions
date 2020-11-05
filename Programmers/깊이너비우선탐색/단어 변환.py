def isConvertable(word1, word2):
    match_num = 0
    for a,b in zip(word1, word2):
        if a == b:
            match_num += 1
    return True if match_num == 2 else False
def dfs(begin, target, words, visited, count):
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if isConvertable(stack, target):
            return count
        for i in range(len(words)):
            if isConvertable(stack, words[i]):
                if visited[i] == 1:
                    continue
                visited[i] = 1
                stacks.append(words[i])
                print(words[i])
        count += 1
    return count

def solution(begin, target, words, count = 0):
    if target not in words:
        return 0
    visited = [0 for i in words]
    return dfs(begin, target, words, visited, 0)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
