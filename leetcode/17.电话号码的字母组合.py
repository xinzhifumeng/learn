#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#字典 加回溯，本题没有终止条件，所有情况都遍历了 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return list()

        dict1={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        def backtrack(index:int):
            if index==len(digits):
                #控制长度
                combinations.append("".join(combination))
                #无空格连接字符，并append
            else:
                digit=digits[index] 
                #分开赋值,此处赋值的是字符串
                for letter in dict1[digit]:  
                    #digit是str，查字典得字母区间
                    combination.append(letter)
                    backtrack(index + 1)
                    #单独这一行就类似递归，当有pop存在就回返回上一个选项中的其他可能项
                    combination.pop()
                    #默认值-1，清空刚刚添加的项，方便循环中下次添加

        combination = list()
        #print输出后可以看到combination是空的list
        combinations = list()
        backtrack(0)
        
        return combinations


# @lc code=end

