#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        #Python isalnum() 方法检测字符串是否由字母和数字组成。
        #Python lower() 方法转换字符串中所有大写字符为小写。
        return sgood == sgood[::-1]


# @lc code=end

