#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#medium-真心没看懂啥意思
'''
给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。

 

示例 1：

输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
示例 2：

输入：a = "a", b = "aa"
输出：2
示例 3：

输入：a = "a", b = "a"
输出：1
示例 4：

输入：a = "abc", b = "wxyz"
输出：-1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-string-match
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 得到满足任何条件的最小叠加字符串new_str
        # 如果a可以作为子串，此时的new_str中一定含有正确答案
        res = len(b) // len(a) if len(b) // len(a) != 0 else 1
        new_str = a * (res + 2)
        for i in range(len(new_str) - len(b) + 1):
            if new_str[i] == b[0]:
                # 当能在new_str中找到b时进行判断
                if new_str[i:i + len(b)] == b:
                    # 从后面看，剩余长度超过2*len(a)的情况
                    if len(new_str) - i - len(b) >= 2 * len(a):
                        return res
                    # 长度超过len(a)的情况
                    elif len(new_str) - i - len(b) >= len(a):
                        return res + 1
                    else:
                        return res + 2

        return -1
# @lc code=end

