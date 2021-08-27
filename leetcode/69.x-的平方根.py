#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#输出为整型，直接二分查找暴力解是可以的
#这里采用牛顿迭代法

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 :return 0
        c,x0=float(x),float(x)
        
        while True:
            xi=0.5*(x0+c/x0)
            if abs(x0-xi)<1e-7:
                break
            x0=xi
        
        return int(x0)
# @lc code=end

