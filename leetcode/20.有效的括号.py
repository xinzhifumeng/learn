#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict1= {'(':')','{':'}','[':']' ,'?':'?'}
        stack=['?']
        for c in s:
            if c in dict1.keys():stack.append(c)
            elif dict1[stack.pop()]!= c:return False;break
        return len(stack)==1


# @lc code=end

