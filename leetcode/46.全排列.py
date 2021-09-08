#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#回溯入门题-类似39

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
#库函数一次搞定       return list(itertools.permutations(nums)) 

        res=[]
        def backtrack(nums, ans):
            
            if len(nums)==0:
                res.append(ans)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], ans + [nums[i]])

        backtrack(nums, [])   
        return res
# @lc code=end

