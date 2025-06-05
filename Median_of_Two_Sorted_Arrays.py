# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1+nums2)
        temp_len = len(nums3)//2
        med = 0
        if len(nums3) % 2 == 0:
            med = float(nums3[temp_len] + nums3[temp_len-1])/2
        else:
            med = nums3[temp_len]
        return med


        
