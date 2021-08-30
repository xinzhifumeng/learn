#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#双指针解题

# @lc code=start
class Solution:
     def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
#官方up 自己的down

'''    
    def maxArea(self, height: List[int]) -> int:
        s=0
        res=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]>height[j]:
                s=height[j]*(j-i)
                j+=-1
            else:
                s=height[i]*(j-i)
                i=i+1
            res=max(s,res)    
        return res
'''
# @lc code=end

