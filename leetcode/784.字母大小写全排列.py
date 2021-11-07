#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#medium
'''
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

 

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #递归
        ans = []
        
        def backtrack(S, p):
            ans.append(S)
            for k in range(p, len(S)):
                if 'a' <= S[k] <= 'z':
                    backtrack(S[:k]+S[k].upper()+S[k+1:], k+1)
                elif 'A' <= S[k] <= 'Z':
                    backtrack(S[:k]+S[k].lower()+S[k+1:], k+1)
            return
        
        backtrack(s, 0)
        return ans

 


# @lc code=end

