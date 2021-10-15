#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#easy
'''
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

 

示例 1：

输入：n = 1
输出：true
解释：20 = 1
示例 2：

输入：n = 16
输出：true
解释：24 = 16

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        while n > 1:
            
            if n % 2 != 0 : return False 
            n = n // 2 
        return n == 1
# @lc code=end

