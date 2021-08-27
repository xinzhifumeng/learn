#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if m==0 and n==0:return 0
        elif m==0 and n==1:return nums2[0]
        elif n==0 and m==1:return nums1[0]

        nums1[m:]=nums2
        nums1.sort()
        if (m+n)/2 != (m+n)//2:
            return nums1[(m+n)//2]
        else:
            a=nums1[(m+n)//2]+nums1[(m+n-2)//2]
            return float(a/2)
# @lc code=end

