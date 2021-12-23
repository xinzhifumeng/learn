#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#easy
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #方法1：排序计数，类似动态规划
        #方法2：排序，取中间值
        nums.sort()
        return nums[len(nums) // 2]
        #方法3：哈希表
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
        
# @lc code=end

