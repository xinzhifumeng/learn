#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(nums, ans):
            
            if len(nums)==0:
                res.append(ans)
                return
            for i in range(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:continue
                backtrack(nums[:i]+nums[i+1:], ans + [nums[i]])

        backtrack(nums, [])   
        return res
# @lc code=end

