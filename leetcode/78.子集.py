#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n=len(nums)
        if n == 0 : return nums
        
        def dfs(num:int,target,res_list):            
            if target == 0:
                res.append(res_list)
            for i in range(num,n):       
                dfs(i+1,target-1,res_list+[nums[i]])

        
        for  k in range(0,n+1):
            dfs(0,3,[])
            
        return res
# @lc code=end

