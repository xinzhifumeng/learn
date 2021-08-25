#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=0
        a=x
        while x!=0 and x>0 and -2**31<a and a <2**31-1:
            if x > 0:
                temp=x%10
                res= res*10+temp
                x=(x-temp)//10
            
        else:
            if res == a : 
                return True
            else:
                return False


# @lc code=end

