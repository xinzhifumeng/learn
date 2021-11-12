#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#中心扩展法可能更合适-medium
'''
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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

