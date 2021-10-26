#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
# @lc code=start
class Solution:
    '''
    def twoSum(nums,target):
        lens=len(nums)
        j=-1
        for i in range(lens):
            for j in range(i,lens):
                if nums[i]+nums[j]==target:
                    #print('{',i,j,target,'}\n')
                    return [i,j]
                else:continue
    '''
     
    
    def twoSum(self, nums, target):
        lens=len(nums)
        j=-1
        for i in range(1,lens):
            temp=nums[:i]
            if (target-nums[i] ) in temp:
                j=temp.index(target-nums[i])
                return [j,i]
                break
        
        

             
    '''
    def twoSum3(nums, target):
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i

    nums=[1,2,3,4,5,6,7,8,9,10]
    twosum(nums,9)
    print(twosum2(nums,9))
    '''
# @lc code=end

