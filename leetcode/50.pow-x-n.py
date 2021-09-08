#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#快速幂方法+递归或迭代

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #递归方法
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)




'''
        def quickMul(N):#迭代-这里为了保持更递归结构一致重新定义了一个函数，完全可以不用
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
            #有点类似2进制，要么1个要么0个，所以一个if就可以判断
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

'''
        
        
'''  笨办法，直接迭代，未加结果判定条件，submi未通过 
        i=1
        
        if n==0: return 1
        elif n<0:x=1/x;n=-n
        pow_num=x
        while i < n:
            pow_num=pow_num*x
            i+=1
        return pow_num
'''

# @lc code=end

