#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid) #n行
        m=len(grid[0]) #m列
        

        f =  [ [0] * (m ) for _ in range(n )]
        f[0][0]=grid[0][0]
        for i in range(1,n):
            f[i][0]=grid[i][0]+f[i-1][0] 
        for j in range(1,m):
            f[0][j]=grid[0][j]+f[0][j-1]
        #print(f)

        
        for j in range(1, m):
            for i in range(1, n):
                f[i][j]=min(f[i-1][j],f[i][j-1])+grid[i][j]
                
        return f[n - 1][ m- 1]
    
# @lc code=end

