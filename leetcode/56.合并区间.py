#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#排序+贪心解题

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret=[]
        start,end=intervals[0]

        for i in intervals:
            if i[0]>end:
                ret.append([start,end])#排出旧区间
                start=i[0]#生成新区间
            end=max(end,i[1])#则更新end，旧区间或新区间
        ret.append([start,end])

        return ret

# @lc code=end

