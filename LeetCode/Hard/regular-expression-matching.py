class Solution:
    import re
    def isMatch(self, s: str, p: str) -> bool:
        return re.match(p, s)