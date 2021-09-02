#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    
        # 将被除数和除数转化为正数
        #倍增法果然妙不可言
        sign = 1
        if divisor * dividend < 0:  # 如果符号不同，则结果返回要变成负数
            sign = -1
            divisor = abs(divisor)
            dividend = abs(dividend)

        elif divisor < 0 and dividend < 0: # 如果被除数和除数都是负值，结果不修改符号
            divisor = abs(divisor)
            dividend = abs(dividend)

        remain = dividend  # 余数
        result = 0  # 商
        while remain >= divisor: 
            cur = 1 # 倍增商
            div = divisor # 倍增值
            while div + div < remain:
                cur += cur 
                div += div 
            remain -= div  # 余数递减
            result += cur  # 商值累计
        
        if sign==-1:  
            result = -result
        
        if result>=2**31:  # 按照题目要求，溢出处理
            result = 2**31-1

        return result
    

    #迭代法
    


    '''    
        temp=abs(dividend)-abs(divisor)
        if temp<0:return 0
        if divisor==0 :return 0
        n=1

        while temp>=abs(divisor):
            temp=temp-abs(divisor)
            n+=1

        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):n=-n
        
        if n>=2**31: return 2**31-1
        elif n<=-2**31:return -2**31
        
        return n
'''
# @lc code=end

