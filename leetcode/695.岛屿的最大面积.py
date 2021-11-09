#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#medium
'''
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

 

示例 1：


输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
示例 2：

输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    
    # 定义深度优先搜索，定义4个位移方向，进行迭代遍历
    # 优点是简单易懂，缺点是容易爆栈
    def dfs(self, grid, r, c): 
        grid[r][c] = 0 # 将遍历的位置改为0
        nr, nc = len(grid), len(grid[0])
        ans = 1
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:
                ans += self.dfs(grid, x, y)
                
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        
        res = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] != 0:
                    res = max(res, self.dfs(grid, r, c))
                    # 一旦出现1，进行dfs，dfs已经不受rc限制了，直到所有的值为0
        
        return res

# @lc code=end

