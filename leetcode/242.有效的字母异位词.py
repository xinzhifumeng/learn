#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
'''

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false


作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = Counter(s)
        t_ = Counter(t)
        return s_ == t_
        #利用哈希表（dict），判断是否里面字符出现的次数时一致的
        #Counter是一种特殊的字典，用两个for循环也可以做

        '''
        l_l = list(s)
        l_l.sort()
        s_l = "".join(l_l)
        l_r = list(t)
        l_r.sort()
        s_r = "".join(l_r)
        return s_l == s_r
        '''
        #等价于return sorted(list(t))==sorted(list(s))


# @lc code=end

