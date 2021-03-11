class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
print(Solution().twoSum([1,2,3,4,5,6,7,8], 15))