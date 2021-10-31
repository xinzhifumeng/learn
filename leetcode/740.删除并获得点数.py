#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#medium
'''
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-and-earn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #对于该题的理解类似于rob的解法，不相邻且同一个数字全部能偷完
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        #形成一个空数列
        for val in nums:
            total[val] += val
        #将空数列填充，横坐标为val，内容为该val的和
        #该数列使用打家劫舍算法
        
        def rob(nums: List[int]) -> int:
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)
            return second
        
        return rob(total)

# @lc code=end

