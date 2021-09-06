#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        #递归的方法最靠谱
        if (n==1):return'1'
        elif n==2:return '11'
        else:
            res=''
            s=self.countAndSay(n-1)
            i=1    
            num=1        
            while i < len(s) :
                
                if s[i]==s[i-1]:
                    num+=1
                elif s[i] != s[i-1]:
                    res+=str(num)+s[i-1]
                    num=1     
                i+=1
            res+= str(num)+s[i-1]
            return res

# @lc code=end

