#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:return 0
        nums.sort()
        nums=nums[::-1]
        
        return nums[k-1]



# @lc code=end

