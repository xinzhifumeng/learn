#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#利用字典

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))#转换为元组，针对字典会返回key组成的tuple
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())

'''主要是dict.get()函数的理解
dict.get(key, default=None)
1. key -- 字典中要查找的键。
2. default -- 如果指定键的值不存在时，返回该默认值。

还有一点要注意：因为字典的键，必须是不可变类型，所以用tuple。

作者：meng-zhi-hen-n
链接：https://leetcode-cn.com/problems/group-anagrams/solution/python3-99-by-meng-zhi-hen-n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''




''' 过于牛逼，没看懂     
#于互为字母异位词的两个字符串包含的字母相同，
#因此对两个字符串分别进行排序之后得到的字符串一定是相同的，
#故可以将排序之后的字符串作为哈希表的键。     
            mp = collections.defaultdict(list)

            for st in strs:
                key = "".join(sorted(st))
                mp[key].append(st)
        
            return list(mp.values())
'''


# @lc code=end

