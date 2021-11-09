#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#medium
'''
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。

 

示例 1：


输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 因为包含两个字符串，所以动态规划需要包含两个维度，在状态转移方程中涉及到左右上下的判定
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 +len2 != len3): return False
        #定义状态方程的矩阵，包含00点
        dp =[[False]*(len2 + 1) for i in range(len1+1)]
        dp[0][0] = True
        # 对初始行列进行定义，类似于最后的定义
        for i in range(1,len1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1]) #对于s1的状态转移
        for i in range(1,len2+1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])  
        
        for i in range(1, 1 + len1 ):
            for j in range(1, 1 + len2):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]

# @lc code=end

