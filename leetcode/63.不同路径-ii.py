#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#62动态规划解题后升级增加了障碍物
#

# @lc code=start

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid) #n行
        m=len(obstacleGrid[0]) #m列
        
        
        f =  [ [0] * (m ) for _ in range(n )]
        if obstacleGrid[0][0]==1:return 0
        else: f[0][0]=1
        
        for i in range(1,n):
            if obstacleGrid[i][0]==1:f[i][0]=0
            else:f[i][0]=f[i-1][0]
        for j in range(1,m):
            if obstacleGrid[0][j]==1:f[0][j]=0
            else:f[0][j]=f[0][j-1]

        
        print(f)
        for j in range(1, m):
            for i in range(1, n):
                '''
                if i-1==0 and obstacleGrid[i-1][j]==1:
                    f[i-1][j]=0
                    
                if j-1==0 and obstacleGrid[i][j-1]==1:
                    f[i][j-1]=0
                '''    
                
                if obstacleGrid[i][j]==1 :f[i][j]=0
                else:f[i][j] = f[i - 1][j] + f[i][j - 1]
                
        return f[n - 1][ m- 1]


'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
         #新建矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])
        store = [[0]*width for i in range(height)]

        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if not obstacleGrid[m][n]: #如果这一格没有障碍物
                    if m == n == 0: #或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m-1][n] if m!=0 else 0 #上方格子
                        b = store[m][n-1] if n!=0 else 0 #左方格子
                        store[m][n] = a+b
        return store[-1][-1]

'''     
       


# @lc code=end

 