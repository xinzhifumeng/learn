#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#medium
'''
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash={0:1}
        sum=0
        count=0
        for i in range(len(nums)):
            sum+=nums[i]
            if((sum-k) in hash):
                count+=hash[sum-k]
            if(sum in hash):
                hash[sum]+=1
            else:
                hash[sum]=1
        return count
'''
作者：wu_yan_zu
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/ha-xi-biao-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

