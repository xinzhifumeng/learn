#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right=0
        
        res=0
        if len(nums)==1 and nums[0]==1:return 1
        elif len(nums)==1 and nums[0]==0:return 0
        while left<len(nums):
            if nums[left]==0 :
                left+=1
                continue
            right+=1
            while right<len(nums) and nums[left]==nums[right]  :
                right+=1
            res=max(right-left,res)
            left=right
        return res
        
# @lc code=end

