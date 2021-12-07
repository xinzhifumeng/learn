#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#搜索矩阵中是否有目标值
#二分法-medium

'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:return False
        m=len(matrix)
        n=len(matrix[0])

        left = 0
        right = m * n - 1
        while left <= right: 
            mid = left + (right - left) // 2
            ans = matrix[mid // n][mid % n]
            
            if target < ans :
                right = mid - 1
                
            elif target > ans :
                left = mid + 1
            
            else:return True

        return False

# @lc code=end

