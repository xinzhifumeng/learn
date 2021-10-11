#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#hard 
'''
将非负整数 num 转换为其对应的英文表示。

 

示例 1：

输入：num = 123
输出："One Hundred Twenty Three"
示例 2：

输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"
示例 3：

输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4：

输入：num = 1234567891
输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-english-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0 : return "Zero"

        def recursion(num: int) -> str:
            s = ""
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + " "
            elif num < 20:
                s += teens[num - 10] + " "
            elif num < 100:
                s += tens[num // 10] + " " + recursion(num % 10)
            else:
                s += singles[num // 100] + " Hundred " + recursion(num % 100)
            return s

        s = ""
        unit = int(1e9) #10^9代表的单位 是32位10进制的上限
        for i in range(3, -1, -1): #3210 四次循环，对应thousands四个位置
            curNum = num // unit
            if curNum:
                num -= curNum * unit #删掉将要表示的数字
                s += recursion(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()




# @lc code=end

