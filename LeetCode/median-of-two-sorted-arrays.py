class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        newList = sorted(nums1 + nums2)
        return len(newList)%2 != 0 and newList[len(newList)//2] or ((newList[len(newList)//2 - 1] + newList[len(newList)//2])/2)

# import statistics
# class Solution:
#     def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
#         return statistics.median(nums1+nums2)


print(Solution.findMedianSortedArrays(0, [1,2,3], [4,5,6]))