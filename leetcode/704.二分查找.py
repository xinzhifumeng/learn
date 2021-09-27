#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xexoac/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        n=len(nums)
        right=n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:return mid
            elif nums[mid] > target:right = mid - 1
            elif nums[mid] < target:left = mid + 1
        return -1



# @lc code=end

