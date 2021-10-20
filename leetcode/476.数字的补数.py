#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#easy
'''
给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

 

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-complement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        highbit = 0
        for i in range(1, 30 + 1):
            if num >= (1 << i):
                highbit = i
            else:
                break
        
        mask = (1 << (highbit + 1)) - 1
        return num ^ mask




# @lc code=end

