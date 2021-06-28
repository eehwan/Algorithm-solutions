class Solution:
    def reverse(self, x: int) -> int:
        if 0 <= x:
            answer = int(str(x)[::-1])
        else:
            answer = -int(str(x)[-1:0:-1])
        if answer >= 2**31-1 or answer <= -2**31: return 0
        else: return answer
        