#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        l=len(nums)
        if l<=1 :return nums

        left=-1
        right=-1
        temp=nums[-1]
        while left>-l and nums[left]>=temp:
            temp=nums[left]
            left+=-1
        while right >left and nums[right]<=nums[left] :
            right+=-1
        #利用双指针从右侧开始判断可替换的位置left，接着找到最接近left且大于的right
        #此时[large (right) left small]注意left替换后left右侧也是个降序

        i=0
        j=l-1
        if right>left:
            nums[left],nums[right]=nums[right],nums[left]
            i=left+l+1
        #如果是降序的数列则if不成立，反之对left右侧进行从新排序即可
        while i<j:#lj直接有小到大重排序
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=-1
        


        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

