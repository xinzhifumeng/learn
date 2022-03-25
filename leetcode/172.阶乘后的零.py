#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#medium
'''
整数 n ，返回 n! 结果中尾随零的数量。
'''
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans


# @lc code=end

