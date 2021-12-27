#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#easy
'''
给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

 

示例 1：

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]
示例 2：

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/occurrences-after-bigram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [words[i] for i in range(2, len(words)) if words[i - 2] == first and words[i - 1] == second]
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/occurrences-after-bigram/solution/bigram-fen-ci-by-leetcode-solution-7q3e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

