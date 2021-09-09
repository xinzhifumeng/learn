#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#寻找数学规律最简单
#动态规划

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #每一格的路径由下方和右方的格子的和决定，最下和最右为边界，从右下开始迭代即可,此处是180度颠倒的
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        #print(f)
        for i in range(1, m):
            for j in range(1, n):
                
                f[i][j] = f[i - 1][j] + f[i][j - 1]
                
        return f[m - 1][n - 1]
        
        
        #return comb(m + n - 2, n - 1)
        

# @lc code=end

