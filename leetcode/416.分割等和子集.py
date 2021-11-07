#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#medium
'''
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        #对数组进行一些判定
        
        #动规 nums[i][target] 二维数组，target由小到大迭代
        #数组从左到右，自上而下进行更新状态
        #由于是自上到下的，所以之前的[i-1][target-nums[i]]中不包含i

        dp= [[False] * (target +1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        # 定义二维数组，targe包含了零，其位置要向后顺一位
        dp[0][nums[0]] = True
        # 前面判断过最大值不会超过一半了，这里对于该值就可以直接定义True
        for i in range(1,n):
            num = nums[i]
            for j in range(1, target + 1):
                # 状态方程
                if j >=num:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
                    # 前面对应如果没有num成立，则该组也成立
                    # 后面对应t继承arget-num是否成立，多次继承知道dp[0][0]
                else:
                    dp[i][j] = dp[i - 1][j]
                    # 此时与num关系不大，直接继承前面的成立关系
        return dp[n - 1][target]


# @lc code=end

