#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#mediun
'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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

