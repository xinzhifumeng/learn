#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

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

