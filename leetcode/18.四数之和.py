#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#只是针对了三数之和进行了修改，一定有更优化的算法
#medium
'''
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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

