#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#同一个最对出现两次

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j
# @lc code=end

