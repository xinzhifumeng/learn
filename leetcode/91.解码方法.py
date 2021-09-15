#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]
        #此处主要考虑新加一位数字带来的影响，f[i]继承之前的数目，
        # 新加入的数字如果能与最后一位配合，则意味着多了一个方法



        '''        
        n=len(s)
        a,b,c=0,1,0
        for i in range(1,n+1):
            c=0
            if s[i-1] != '0':
                c+=b
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <=26:
                c+=a
            a,b = b,c
        return c 
        '''
# @lc code=end

