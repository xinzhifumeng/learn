#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#easy
'''
有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。

给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。

 

示例 1：

输入：S = "5F3Z-2e-9-w", K = 4
输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。
示例 2：

输入：S = "2-5g-3-J", K = 2
输出："2-5G-3J"
解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/license-key-formatting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = list()
        cnt = 0

        for i in range(len(s) - 1, -1, -1):#根据题意，用逆序处理最合适
            if s[i] != "-":
                ans.append(s[i].upper())
                cnt += 1
                #通过计数来增加-，最后消掉最前面的-
                if cnt % k == 0:
                    ans.append("-")
        
        if ans and ans[-1] == "-":
            ans.pop()
        
        return "".join(ans[::-1])



# @lc code=end

