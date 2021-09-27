#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#二分法解题
'''
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

 

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xe6xnr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
                    #通过计数来确定mid前面有没有重复的数字
                    #mid 代表了下标，小了则意味着下标前有重复的
                    #num数组只在计数的时候起作用，消除LR边界
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left
'''
作者：Nicosauto
链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/python-xun-zhao-zhong-fu-shu-by-nicosaut-o8zu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=end

