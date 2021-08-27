#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#找规律解只是其中之一的方法比较好理解
#存在更简洁的方法


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        p=0
        q=0
        r=1 
        i=1
        while i <= n :
            p=q
            q=r
            r=p+q
            i+=1
        return r 

# @lc code=end

