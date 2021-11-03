#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] 乘积为正数的最长子数组长度
#medium
'''
给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

 

示例  1：

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。
示例 2：

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
示例 3：

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        length = len(nums)
        positive, negative = [0] * length, [0] * length
        if nums[0] > 0:
            positive[0] = 1
        elif nums[0] < 0:#乘积为负的数组长度
            negative[0] = 1
        
        maxLength = positive[0]
        for i in range(1, length):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1 #这很好理解 +1 而已
                negative[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
                #num为正对negative的个数影响就是+1，除非之前没有负数
                #这里不考虑两个的情况，因为else会避免这种情况
            elif nums[i] < 0:
                positive[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
                #小于0需要对negative进行反转并+1
                # 如果没有的情况下代表这是第一个负数，只会出现在开头和0后面，代表无法反转正整数为个数为0
                negative[i] = positive[i - 1] + 1 #最长正整数个数+1
                #很明显小于零的增加量是在相反的基础上计算的，判定条件都是对开头或0之后有效的，
            else:
                positive[i] = negative[i] = 0
            #print(positive,negative)
            maxLength = max(maxLength, positive[i])
            #在没有每次取max之前，两个值对应num为负时过于依赖对方的值，有时反转后的值不一定大于原来叠加的值
            #仔细看该题可以发现n的递增序列是交替出现在两数组中的，n为0分割的子数组长度
        return maxLength


        
        '''
        #由于存在复数，需要维护两个数组min and max
        #最大乘积的解法
        length = len(nums)
        dp_max= [nums[0]] + [0] * (length - 1)
        dp_min= [nums[0]] + [0] * (length - 1)
        
        for i in range(1,length):
            dp_max[i] = max( nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
            dp_min[i] = min( nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
        return dp_max[length - 1]
        '''

# @lc code=end

