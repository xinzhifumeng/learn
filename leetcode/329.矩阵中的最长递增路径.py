#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#hard
'''
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

 

示例 1：


输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：


输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：

输入：matrix = [[1]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        flag = [[-1] * n for _ in range(m)] #存储从（i，j）出发的最长递归路径

        def dfs(i, j):
            if flag[i][j] != -1: # 记忆化搜索，避免重复的计算
                return flag[i][j]
            else:
                d = 1
                for (x, y) in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    x, y = i + x, j + y
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        d = max(d, dfs(x, y) + 1) # 取四个邻接点的最长
                flag[i][j] = d
                return d

        res = 0
        for i in range(m): # 遍历矩阵计算最长路径
            for j in range(n):
                if flag[i][j] == -1:
                    res = max(res, dfs(i, j))
        return res
'''
作者：lzx1997
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ji-yi-hua-de-di-gui-sou-suo-by-lzx1997-v49k/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=end

