# Calculate median of two sorted arrays
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        if len(nums1) == 1: return nums1[0]
        nums1.sort()
        
        if len(nums1) % 2 == 1:
            return nums1[(len(nums1)) // 2]
        else:
            print(len(nums1) // 2)
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
