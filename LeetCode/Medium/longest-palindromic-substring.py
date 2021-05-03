class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for l in range(length):
            for i in range(l+1):
                word = s[i:length-l+i]
                if word == word[::-1]:
                    return word
