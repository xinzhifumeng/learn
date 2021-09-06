#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import Text


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #二分法
        if not nums:return -1
        l=len(nums)
        
        left=0
        right=l-1
        while left <=right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
# @lc code=end

