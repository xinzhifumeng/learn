#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
'''
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

 

示例 1：

输入：num = 16
输出：true
示例 2：

输入：num = 14
输出：false

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xel3tc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1 : return True
        left, right = 0 , num
        while left < right:
            mid = (left + right) // 2
            if mid * mid == num: return True
            if mid * mid > num: right = mid 
            elif mid * mid < num: left = mid + 1 
        return False
# @lc code=end

