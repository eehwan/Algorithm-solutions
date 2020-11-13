from collections import deque

def isConvertable(word1, word2):
    unmatch = sum(a != b for a,b in zip(word1, word2))
    return unmatch == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = {key:0 for key in words}
    queue = deque()
    queue.append(begin)
    while queue:
        current = queue.popleft()
        if current == target:
            return visited[current]
        for word in words:
            if visited[word] != 0:
                continue
            if isConvertable(current, word):
                # print(word)
                queue.append(word)
                try:
                    visited[word] = visited[current] + 1
                except:
                    visited[word] = 1
                # print(visited)
        # print(queue)
    return 0
print(solution("hit", "hhh", ["hht","hhh", "dod", "dog", "lot", "cog"]))
