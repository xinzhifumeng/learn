#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={
            "I":1,
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
            }
        sum=0
        i=0
        while (i<len(s)):
            if s[i:i+2] in dict1.keys():
                sum+=dict1[s[i:i+2]]
                i=i+2
            elif s[i] in dict1.keys():
                sum+=dict1[s[i]]
                i=i+1
        return sum

# @lc code=end

