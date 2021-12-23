#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#medium
'''
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

 

示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            # 迭代p235，去求下一个丑数，并赋值给dp[i]
            dp[i] = min(num2, num3, num5)
            #赋值后改变进行下一个的迭代，这里采用了三个if句子
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]
        #官方采用了动归的解法，从结果上来看，没一个数下对应了到该位置丑数的数目
        #
        
        #个人认为可以用if加for循环，这样最简单


# @lc code=end

