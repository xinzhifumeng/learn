#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#easy
'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

 

示例 1：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

根据我们的探索，我们猜测会有以下三种可能。

最终会得到 11。
最终会进入循环。
值会越来越大，最后接近无穷大。
'''

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_sum = 0
            while n > 0 :
                n, digit =divmod(n, 10) 
                # n=n///10 digit=m%10
                total_sum += digit ** 2
            return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n==1


        
# @lc code=end

