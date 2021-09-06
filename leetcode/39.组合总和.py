#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#回溯法

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []
        def backtrack(candidates,target,res_list):
            if target < 0:
                return
            if target == 0:
                res.append(res_list)
            for i,c in enumerate(candidates):
                # 为了避免重复 (例如candiactes=[2,3,6,7],target=7，输出[[2,2,3],[3,2,2][7]])
                # 传到的下一个candicate为candicates[i:]
                backtrack(candidates[i:],target-c,res_list+[c])
        
        backtrack(candidates,target,[])
        return res
         
            

# @lc code=end

