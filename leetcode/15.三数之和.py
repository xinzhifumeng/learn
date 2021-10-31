#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和-双指针-固定第一个数
#meidum
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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

