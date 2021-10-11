#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#medium
'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start


class Solution:
    def numSquares(self, n: int) -> int:

        '''
        if n == 0:
            return 0
        rg = int(sqrt(n))
        ans = inf
        for i in range(rg,0,-1):
            ans = min(ans, self.numSquares(n-i*i) + 1)
        return ans
        '''
    '''
    作者：himymBen
    链接：https://leetcode-cn.com/problems/perfect-squares/solution/python-xin-de-yi-tian-xin-de-ji-yi-hua-s-p4bc/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''    
    
    ans = inf  #这里inf是什么意思？？正无穷
    def numSquares(self, n: int) -> int:
        return self.answer(n, 0)

   
    def answer(self, n, ans):
        if ans >= self.ans:
            return inf
        if n == 0:
            self.ans = ans
            return ans
        rg = int(sqrt(n))
        res = inf
        for i in range(rg, rg//2, -1):
            res = min(res, self.answer(n - i * i, ans + 1))
        return res
        
'''
利用 inf 做简单加、乘算术运算仍会得到 inf
>>> 1 + float('inf')
inf
'''

# @lc code=end

