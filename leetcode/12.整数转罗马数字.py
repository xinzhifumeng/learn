#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"] # 1000，2000，3000
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100~900
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10~90
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1~9
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
    #直接暴力匹配-空间复杂度减小，运算加快


'''
    def intToRoman(self, num: int) -> str:
        dict1={
            1000:'M',
            900:"CM",
            500:'D', 
            400:"CD",
            100:'C',
            90:"XC",
            50:'L', 
            40:"XL",
            10:'X',
            9:"IX",
            5:'V',
            4:"IV",
            1:'I'
            } #必须按顺序排列才能匹配
        res=''
        for key in dict1:
            if num//key !=0:
                count=num//key
                res+=dict1[key]*count
                num%=key
        return res
#哈希（字典）匹配
'''

'''
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
#罗马转数字
'''        
# @lc code=end

