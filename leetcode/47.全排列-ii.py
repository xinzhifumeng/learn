#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(nums, ans):
            
            if len(nums)==0:
                res.append(ans)
                return
            for i in range(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:continue
                backtrack(nums[:i]+nums[i+1:], ans + [nums[i]])

        backtrack(nums, [])   
        return res
# @lc code=end

