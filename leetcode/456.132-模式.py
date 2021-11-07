#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132 模式
#medium
'''
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。

如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
示例 2：

输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
示例 3：

输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #单调栈
        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
            # 遍历一遍，从左到右更新出来132中的1，确保判定时存在1
        stack = []
        for j in range(N - 1, -1, -1):# 反向遍历
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]: 
                #保证第一个数不入栈
                numsk = stack.pop()                
                # 大于nums[j+]的nums[j] 则执行出栈，对出栈的数进行判定
                # 此时nums[j] 是作为3存在的 多次排出栈的作为2进行判定
                # 所有的2都不符合条件刚好被排出栈 ，3入栈
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False




        '''
        # 暴力解 超时
        N = len(nums)
        numsi = nums[0]
        for j in range(1, N): #num[j]需要大于numi
            if nums[j] <= numsi:
                numsi = nums[j]
            else:
                for k in range(N - 1, j, -1):
                    if numsi < nums[k] and nums[k] < nums[j]:
                        return True
            
        return False
        '''

# @lc code=end

