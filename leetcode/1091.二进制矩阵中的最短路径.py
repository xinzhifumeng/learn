#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
# medium
'''
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

 

示例 1：


输入：grid = [[0,1],[1,0]]
输出：2
示例 2：


输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4
示例 3：

输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if grid[0][0] != 0 or grid[l-1][l-1] != 0:  #处理特殊情况
            return -1
        if l == 1:
            return 1

        visited = set((0,0)) #存放已遍历的位置的集合
        Q  = collections.deque([(0,0)])  #存放接下来一轮的地址
        Q2 = collections.deque([])       #在一轮中暂存所有的位置
        ans = 0

        while Q:
            ans += 1
            while Q:  #首先把此轮中Q内所有点的周围遍历过去，为了方便记录ans，每次都遍历完后，才把新的点重新加入
                i, j = Q.popleft()
                if i == l-1 and j == l-1:   #发现已经找到终点，那就可以直接返回了
                    return ans
                for (x, y) in [(i-1,j),(i+1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]:
                    if (x,y) not in visited and l>x>=0 and l>y>=0:
                        if grid[x][y] == 0:
                            visited.add((x,y))
                            Q2.append((x,y))
            while Q2:   #把Q2中的下一轮需要遍历的点加回到Q中
                Q.append(Q2.popleft())
        return -1   #遍历完了还没到达终点，说明根本无法过来
'''
作者：bluegreenred
链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/solution/1091-er-jin-zhi-ju-zhen-zhong-de-zui-dua-vgdw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

