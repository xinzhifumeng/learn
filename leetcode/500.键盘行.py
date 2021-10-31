#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#easy

'''
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。


 

示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
先把26个字母进行编码，同一行的编码一致
每个字母对应一个数组下标
比如 a 对应 index = 0，z 对应 index = 23
对于每个单词，挨个遍历，计算他们的编码
注意单词的大小写，将字符转成数组的下标进行获取编码
比如 a 要转成 index = 0， 可以用 ord(w) - ord('a'), ord()ord()函数可以返回一个字符对应的ASCII编码，再减去 aa 的ASCII编码即可获得对应的index
如果每个字母的编码都一致，就放到最终结果里

作者：niconiconi-12
链接：https://leetcode-cn.com/problems/keyboard-row/solution/chi-xiao-dou-nojie-ti-python-ha-xi-biao-z87oo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hash_map = '12210111011122000010020202'
        ans = []
        for word in words:
            idx = hash_map[ord(word[0].lower()) - ord('a')] #定义第一个字母哈希表的值，利用if + for 判定之后的哈希值
            if all(hash_map[ord(w.lower()) - ord('a')] == idx for w in word):
                ans.append(word)
        return ans



# @lc code=end

