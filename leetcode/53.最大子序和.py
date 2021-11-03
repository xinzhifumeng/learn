#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#easy
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
#动态规划
#利用每一项之前的最大值，有效降低重复计算
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#使用暴力法很简单，复杂度n^2,两个循环即可
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        result = dp[0]
        i=1
        while i < len(nums):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            print(dp[i])
            result = max(dp[i], result) 
            i += 1
        
        return result
            

# @lc code=end

