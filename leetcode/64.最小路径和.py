#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#medium
'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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

