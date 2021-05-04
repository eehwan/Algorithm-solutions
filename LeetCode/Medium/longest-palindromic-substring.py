class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for l in range(length):
            for i in range(l+1):
                word = s[i:length-l+i]
                if word == word[::-1]:
                    return word

# Faster Solution
# def longestPalindrome(self, s: str) -> str:
    # if len(s) <= 1:
        # return s
    # i,l=0,0
    # for j in range(len(s)):
        # print(i,j,l)
        # print(j-l, j+1)
        # if s[j-l: j+1] == s[j-l: j+1][::-1]:
            # i, l = j-l, l+1
        # elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
            # i, l = j-l-1, l+2
    # return s[i: i+l]