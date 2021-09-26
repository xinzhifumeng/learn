#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
'''
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set(nums1).intersection(set(nums2)))
        ans,n1,n2=[],set(nums1),set(nums2)
        for n in n1:
            if n in n2:ans.append(n)
        return ans



# @lc code=end

