#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#medium
'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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
            dfs(0,k,[])
            
        return res
# @lc code=end

