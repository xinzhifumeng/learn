#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#medium
'''
给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）

此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

 

示例 1：

输入：[1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3
示例 2：

输入：[5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
示例 3：

输入：[3,-1,2,-1]
输出：4
解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 最大和在中间的话同53题，在两边的话，最大和在两边，减去中间最小和就行
# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp_max = nums[0]
        dp_min = nums[0]

        sum=nums[0]
        result_min = nums[0]
        result_max = nums[0]
        i=1
        while i < len(nums):
            
            dp_max = max(0, dp_max) + nums[i]
            dp_min = min(0, dp_min) + nums[i]
        
            result_max = max(dp_max, result_max) 
            result_min = min(dp_min, result_min)
            sum += nums[i]

            i += 1
        if result_max < 0: return result_max
        return max(result_max, sum - result_min)
# @lc code=end

