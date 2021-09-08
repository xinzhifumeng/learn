#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:return True
         
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i: #向右跳
                maxPos = max(maxPos, i + nums[i])
                if nums[i]==0 and maxPos==i:return False
                if i == end :#最远的位置结束本轮筛选
                    end = maxPos#最远的位置由num[i]决定，end代表本次跳跃的位置
                    step += 1
        return True if step else False
# @lc code=end

