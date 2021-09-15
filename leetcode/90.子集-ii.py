#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#相对于子集1多了去重

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n=len(nums)
        nums.sort()
        if n == 0 : return nums

        
        def dfs(num:int,target,res_list):            
            if target == 0:#加了一个去重的判定
                if len(res) == 0:res.append(res_list)
                elif res_list not in  res: 
                    res.append(res_list)
            for i in range(num,n):  
              
                dfs(i+1,target-1,res_list+[nums[i]])

        
        for  k in range(0,n+1):
            dfs(0,k,[])

        return res
# @lc code=end

