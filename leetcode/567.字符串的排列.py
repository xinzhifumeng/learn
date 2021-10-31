#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#medium
'''
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         # 统计 s1 中每个字符出现的次数
        counter1 = collections.Counter(s1)
        N = len(s2)
        # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
        left = 0
        right = len(s1) - 1
        # 统计窗口s2[left, right - 1]内的元素出现的次数
        counter2 = collections.Counter(s2[0:right])

        while right < N:
            # 把 right 位置的元素放到 counter2 中
            counter2[s2[right]] += 1
            # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
            if counter1 == counter2:
                return True
            # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
            counter2[s2[left]] -= 1
            # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            # 窗口向右移动
            left += 1
            right += 1
        return False



# @lc code=end

