#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#只是针对了三数之和进行了修改，一定有更优化的算法

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans=list()
        if len(nums)<2:return []
        i=1
        j=0
        while j+3<len(nums):
            temp=target-nums[j]
            while i+2<len(nums):
                left=i+1
                right=len(nums)-1
                while  right>left :
                    sum=nums[left]+nums[right]
                    if nums[i]+sum > temp : #值过大，需要righ左移
                        right += -1
                
                    elif nums[i]+sum < temp :#值过小，需要left右移
                        left += 1
                        
                    elif  sum+nums[i]==temp and [nums[j],nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[j],nums[i], nums[left], nums[right]])                        
                        left+=1
                    else:
                        left+=1

                i+=1
            j+=1
            i=j+1
        return ans

# @lc code=end

