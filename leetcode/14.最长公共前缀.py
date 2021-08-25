#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return " "
        res=strs[0]
        i=1
        while (i <  len(strs)):
            while strs[i].find(res) !=0:   #查找字符，返回相符的字符位置n，没有为-1,此处0就是第一位
                res=res[0:len(res)-1]
                print(strs[i].find(res))
            i+=1
        return res  
# @lc code=end

