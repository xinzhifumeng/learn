#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#
'''
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。

 

示例 1：

输入：n = 10, pick = 6
输出：6
示例 2：

输入：n = 1, pick = 1
输出：1

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xee4ev/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                #1 pick>mid
                left = mid + 1
            elif guess(mid)==-1:
                right = mid - 1

        # End Condition: left > right
        return -1

        
# @lc code=end

