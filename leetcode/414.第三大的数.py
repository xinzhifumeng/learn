#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#easy
'''
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

 

示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/third-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=len(nums)
        
        i=-2
        a=1
        nums.sort()
        ans=nums[-1]
        while i >= -l:
            if nums[i] == nums[i+1]:
                i+=-1
                continue
            a+=1
            if a == 3: return nums[i]
            ans=max(ans,nums[i])
            i+=-1
            
        return ans
# @lc code=end

