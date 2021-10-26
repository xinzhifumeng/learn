#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#hard
'''
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

 

示例 1：

输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：

输入：s = ")("
输出：[""]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(self, s: str) -> bool:
            dict1= {'(':')','{':'}','[':']' ,'?':'?'}
            stack=['?']
            for c in s:
                if c in dict1.keys():stack.append(c)
                elif dict1[stack.pop()]!= c:return False;break
            return len(stack)==1

# @lc code=end

