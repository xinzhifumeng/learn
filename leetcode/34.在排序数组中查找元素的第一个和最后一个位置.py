#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#medium
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


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

