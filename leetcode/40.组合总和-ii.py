#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#回溯法

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def combination(candidates,target,res_list,left):
            if target < 0:
                return
            if target == 0:
                res.append(res_list)
            
            for i in range(left, len(candidates)) :
                # 为了避免重复 (例如candiactes=[2,3,6,7],target=7，输出[[2,2,3],[3,2,2][7]])
                # 传到的下一个candicate为candicates[i:]
                if i>left and candidates[i]==candidates[i-1]:continue #第二个数重复则跳过计算
                combination(candidates,target-candidates[i],res_list+[candidates[i]],i+1)
        
        combination(candidates,target,[],0)
        return res


# @lc code=end

