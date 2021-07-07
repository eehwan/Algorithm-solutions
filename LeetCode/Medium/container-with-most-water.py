class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                answer = max(answer, (j-i)*min(height[i], height[j]))
        return answer