class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start, last = 0, len(height) - 1
        while last > start:
            answer = max(answer, (last - start) * min(height[start], height[last]))
            if height[start] > height[last]: last -= 1
            else: start -= 1
        return answer