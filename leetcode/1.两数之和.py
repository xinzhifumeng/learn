#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    
def twosum(nums,target):
    lens=len(nums)
    j=-1
    for i in range(lens):
        for j in range(i,lens):
            if nums[i]+nums[j]==target:
                print('{',i,j,target,'}\n')
                return[i,j]
            else:continue


def twosum2(nums,target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]#采用大于i的做法，类似于两次for循环，更便捷
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i] 

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

# @lc code=end

