#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#medium
'''
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        d, t = nums[0] - nums[1], 0
        ans = 0
        
        # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1 #这里妙在该数组个数是随长度增加的
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t
            
        return ans

# @lc code=end

