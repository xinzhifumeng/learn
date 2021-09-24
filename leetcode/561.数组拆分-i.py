#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        
        sum=0
        l=len(nums)
        while left+1<=l:
            sum+=(min(nums[left],nums[left+1]))
            left+=2
            
        return sum



# @lc code=end

