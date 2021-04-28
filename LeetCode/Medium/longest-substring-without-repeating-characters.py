class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        answer = 0
        start = 0
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                answer = max(answer, i - start)
                start = used[char] + 1
                used[char] = i
            else:
                used[char] = i
            print(i, char, start, answer)
        answer = max(answer, len(s) - start)
        return answer

print(Solution.lengthOfLongestSubstring(0, "abba"))