#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:return 0

        n=len(nums)
        temp=1
        i=1
        while i < n:
            if nums[i]!=nums[i-1]:
                nums[temp]=nums[i]
                temp+=1
            i+=1

        return temp


# @lc code=end

