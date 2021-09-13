#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#感觉应该用递归的方法

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(num:int,target,res_list):
            
            if target == 0:
                res.append(res_list)
            for i in range(num,n+1):
                
                dfs(i+1,target-1,res_list+[i])
        
        dfs(1,k,[])
        return res
         
        
        # @lc code=end

