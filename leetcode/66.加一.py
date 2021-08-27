#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#解法1 转化为数值加1然后转为list 
# list -> str -> int -> str -> list:
#int(str(digits[*]))
# list(str(num))
#解法2 考虑进位问题

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jinwei = 1
        i=-1
        while i  >= -len(digits):
            digits[i]=digits[i]+jinwei
            jinwei=0
            if digits[i]==10 and i!=(-len(digits)):
                digits[i]=0
                jinwei=1
            elif digits[i]==10 and i==(-len(digits)):
                digits[i]=0
                digits.insert(i-1,1)
                jinwei=0
            i+=-1
        return digits
            

# @lc code=end

