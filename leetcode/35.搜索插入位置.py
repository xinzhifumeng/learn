#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#easy
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4
示例 4:

输入: nums = [1,3,5,6], target = 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        #普通方法解-success
        i=0
        while i< len(nums):
            if target<=nums[i]:
                return i
            i+=1
        return len(nums)
        '''    
      
        left=0
        right=len(nums)-1
        while left <= right:
            mid=int((right+left)/2)
            if target > nums[mid]:
                left=mid+1
                ans=left
            elif target < nums[mid]:
                ans=mid
                right=mid-1
            else:return mid
        return ans

        #本题主要想让答题者使用二分法，其算符满足logn复杂度的关系
        
# @lc code=end

