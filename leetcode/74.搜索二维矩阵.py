#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#搜索矩阵中是否有目标值
#二分法


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

