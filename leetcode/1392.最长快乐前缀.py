#
# @lc app=leetcode.cn id=1392 lang=python3
#
# [1392] 最长快乐前缀
#hard
'''
「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。

给你一个字符串 s，请你返回它的 最长快乐前缀。

如果不存在满足题意的前缀，则返回一个空字符串。

 

示例 1：

输入：s = "level"
输出："l"
解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
示例 2：

输入：s = "ababab"
输出："abab"
解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
示例 3：

输入：s = "leetcodeleet"
输出："leet"
示例 4：

输入：s = "a"
输出：""

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-happy-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        # 暴力求解
        n = len(s)
        for i in range(n - 1, 0, -1):
            if s.endswith(s[:i]):
                # 如果字符串以s[:i]的方式结束，则返回true
                return s[-i:]
        return ""
# @lc code=end

