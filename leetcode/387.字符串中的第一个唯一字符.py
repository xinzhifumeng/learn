#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
  
    def firstUniqChar(self, s: str) -> int:  
        '''
        frequency = collections.Counter(s)
        #collections 没太整明白
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
        '''
        '''
        >>>seq = ['one', 'two', 'three']
        >>> for i, element in enumerate(seq):
        ...     print i, element
        ... 
        0 one
        1 two
        2 three
        '''
        #哈希方法 
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            first = -1
        return first

#作者：LeetCode-Solution
#链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-x9rok/


        


# @lc code=end

