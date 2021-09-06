#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        if not nums:return [-1,-1]
        left=0
        l=len(nums)
        while left<l and nums[left] != target:
            left+=1
        
        if left==l:return [-1,-1]
        elif left==l-1:return [l-1,l-1]
        else:
            right=left
            while right<l and nums[right] == target:
                 right+=1
            return [left,right-1]


        
# @lc code=end

