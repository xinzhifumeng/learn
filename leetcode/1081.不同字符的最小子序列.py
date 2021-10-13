#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#medium
'''
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。

注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ## 定义个一个Countet容器来记录s中所有字符的个数
        h = collections.Counter(s)
        
        ##定义一个单调栈
        stack = []

        ## 开始遍历字符串
        for ch in s:
            if ch not in stack:
            ## 判断这个栈顶元素是不是比我们要入栈的元素大，且这个元素是不是不止一个（是不是重复）
            ## 就是贪心的思想。
                while stack and ch < stack[-1] and h[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            h[ch] -= 1
        return ''.join(stack)



# @lc code=end

