#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#官方解答-矩阵操作

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #借助辅助数组
        n=len(matrix)
        #matrix_new=matrix 这么写是引用拷贝，要重新生成矩阵
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:]=matrix_new


'''  原地旋转,必须一下转一组即四个      
        n=len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                temp                 = matrix[i][j]
                matrix[i][j]         = matrix[n-j-1][i]
                matrix[n-j-1][i]     = matrix[n-1-i][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1]     = temp
                
            
        return matrix

'''


# @lc code=end

