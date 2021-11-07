#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#hard
'''
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-good-base
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # n = x^(m-1) + x^(m-2) + ... + x + 1
        for m in range(num.bit_length(),2,-1):
            # 二项式展开 x^(m-1) < n < (x+1)^(m-1)
            # 返回 base 的 exp 次幂；如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）。 
            # 两参数形式 pow(base, exp) 
            # 等价于乘方运算符: base**exp。
            x = int(pow(num,1/(m-1)))
            # 等比数列求和 n = (x^m - 1)/(x-1)
            if num == (pow(x,m) - 1)//(x-1):
                return str(x)
        return str(num-1)
'''
作者：himymBen
链接：https://leetcode-cn.com/problems/smallest-good-base/solution/python-ren-xing-de-py100-by-qubenhao-6kvg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=end

