#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=1
        j=0
        res=1
        if len(s)==0:return 0
        while i < len(s):
            while s[i] in s[j:i] and j<i:
                j+=1
            res=max(res,i-j+1)
            i+=1
        return res


# @lc code=end

