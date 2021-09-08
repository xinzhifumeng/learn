#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#利用了48和59题

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        if not n :
            return n
        matrix = [[0] * n for _ in range(n)]
        l=1
        rows, columns = n,n
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                matrix[top][column]=l;l+=1
            for row in range(top + 1, bottom + 1):
                matrix[row][right]=l;l+=1
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    matrix[bottom][column]=l;l+=1
                for row in range(bottom, top, -1):
                    matrix[row][left]=l;l+=1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix
# @lc code=end

