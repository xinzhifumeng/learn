#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和-双指针-固定第一个数
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans=list()
        if len(nums)<2:return []
        i=0
        while i+2<len(nums):
            left=i+1
            right=len(nums)-1
            while  right>left :
                sum=nums[left]+nums[right]
                if nums[i]+sum > 0 : #值过大，需要righ左移
                    right += -1
                
                elif nums[i]+sum < 0 :#值过小，需要left右移
                    left += 1
                        
                elif  sum+nums[i]==0 and [nums[i], nums[left], nums[right]] not in ans:
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                else:
                    left+=1

            i+=1
            
        return ans


# @lc code=end

