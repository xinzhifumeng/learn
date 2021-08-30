#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        if not nums or len(nums)<3:return []
         
        ans=abs(abs(nums[0])+abs(nums[1])+abs(nums[2])-target)
        res=(abs(nums[0])+abs(nums[1])+abs(nums[2])-target)
        
        i=0
        while i+2<len(nums):
            left=i+1
            right=len(nums)-1
            while  right>left :
                temp = nums[left]+nums[right]+nums[i]-target
                ans=min(ans,abs(temp))

                if ans==abs(temp):
                    res=temp+target
                
                if temp>0:  #值过大，需要righ左移
                    right += -1
                
                else :#值过小，需要left右移
                    left += 1
                        
            i+=1
        return res

#最后一个未通过

# @lc code=end

