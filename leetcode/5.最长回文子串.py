#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#中心扩展法可能更合适

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        right=0
        left=0
        i=1
        res=s[0]

        if len(s)==0:return 0
        elif len(s)==1 or (len(s)==2 and s[0]==s[1]):return s
        elif len(s)==2 and s[0]!=s[1]:return s[0]
        
        while i < len(s)-1:
            
            left=i-1
            right=i+1
            while  right<len(s) and left>=0 and s[left]==s[right]  :
            #沿i向两边扩展
                if (right-left+1>len(res)):
                    res= s[left:right+1]
                left+=-1
                right+=1
            
            left=i-1
            right=i #沿i与i-1向两边扩展
            while right<len(s) and left>=0 and s[left]==s[right]  :
            #有个bug i不会等于n-1，放在循环外单独讨论,放最后不影响res  
                if (right-left+1>len(res)):
                    res= s[left:right+1]
                left+=-1
                right+=1

            i+=1
        if len(s)>2 and s[-1]==s[-2] and len(res)<2:
            res=s[len(s)-2:len(s)]

        return res

# @lc code=end

