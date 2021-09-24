#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#滑动窗口
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:return 0
        n=len(nums)
        ans=n+1
        start,end =0,0
        total=0
        while end < n:
            total +=nums[end]
            while total >= target:#前提条件是必须有成立的数组，感觉有问题啊，加一个判定更合适
                ans=min(ans, end - start +1)
                total -= nums[start]
                start +=1
            end += 1
        return 0 if ans == n+1 else ans

        
# @lc code=end

