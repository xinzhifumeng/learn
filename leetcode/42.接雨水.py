#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#hard
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)

        #更新left_max right_max数组
        left_max = [height[0]] + [0] * (n-1)
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
       
        right_max =[0] * (n-1) + [height[n-1]]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i +1 ], height[i])
        
        #两个数组的交集减去高度就是ans
        #ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        sum = 0
        for i in range(0,n):
            sum += min(left_max[i], right_max[i]) - height[i]
        return sum


# @lc code=end

