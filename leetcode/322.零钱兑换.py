#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#medium
'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
''' 
#简单的方法就是用递归的方法
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #if(amount == 0):return 0
        #这一行可有可无，因为下面两行定义覆盖了amount = 0 的情况

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            #从最小的硬币开始，组成一个个数的数组，知道达到target
            #因为要用到前面的结果，所以从硬币值迭代到target
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                # 引入新硬币后进行对比，新硬币能有效降低个数就采用，从左向右迭代

        return dp[amount] if dp[amount] != float('inf') else -1


        
    
# @lc code=end

