#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i: #向右跳
                maxPos = max(maxPos, i + nums[i])
                if i == end:#最远的位置结束本轮筛选
                    end = maxPos#最远的位置由num[i]决定，end代表本次跳跃的位置
                    step += 1
        return step
# @lc code=end

