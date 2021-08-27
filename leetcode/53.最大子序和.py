#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
#动态规划
#利用每一项之前的最大值，有效降低重复计算

#使用暴力法很简单，复杂度n^2,两个循环即可
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=nums
        result=dp[0]
        i=1
        while i<len(nums):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            result= max(dp[i],result) 
            i+=1
        return result
            

# @lc code=end

