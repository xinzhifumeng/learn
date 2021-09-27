#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnq4km/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:return 0
        size = len(nums)
        if size==1:return nums[0]

        dp=[0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,size):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1]) 
            #每个值都与前面的值的最大值有关
        return dp[size-1]

# @lc code=end

