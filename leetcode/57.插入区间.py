#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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

