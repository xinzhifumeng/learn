#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#medium
'''
给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-digit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        cur, base = 1, 9
        while n > cur * base:
            n -= cur * base
            cur += 1
            base *= 10
        n -= 1
        # 数字
        num = 10 ** (cur - 1) + n // cur
        # 数字里的第几位
        idx = n % cur
        return num // (10 ** (cur - 1 - idx)) % 10
'''
作者：himymBen
链接：https://leetcode-cn.com/problems/nth-digit/solution/pythonjavajavascriptgo-jian-dan-mo-ni-by-kk3x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

