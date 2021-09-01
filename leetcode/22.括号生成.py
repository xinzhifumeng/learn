#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#生成不重复合集，满足有效验证

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        i=0
        if n==0 :return []
        ans=[]
        
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                #这里决定了成立条件--对应规律左括号先出现且多于右括号
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
        #回溯法用画图去理解比较容易

'''
def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return ['']
        ans = []

        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        #递归法 真心没看懂，似乎是left和right作为一个合法的括号序列插入到(left)right中递归
        return ans
'''

            
                   

# @lc code=end

