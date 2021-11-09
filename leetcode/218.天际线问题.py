#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#hard
'''
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

 

示例 1：


输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
示例 2：

输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-skyline-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        s = []
        ans = []
        h = 0
        for left, right, height in buildings:
            while s and s[0][0] < left:
                r, rh = heapq.heappop(s)
                if rh == h:
                    rh = max(s, key=lambda val: val[1])[1] if s else 0
                    if rh != h:
                        h = rh
                        ans.append([r, h])
            if height > h:
                h = height
                # 避免左端点重复的问题
                if ans and left == ans[-1][0]:
                    ans[-1][1] = h
                else:
                    ans.append([left, h])
            heapq.heappush(s, [right, height])
        while s:
            r, rh = heapq.heappop(s)
            if rh == h:
                rh = max(s, key=lambda val: val[1])[1] if s else 0
                if rh != h:
                    h = rh
                    ans.append([r, h])
        return ans
'''
作者：meteordream
链接：https://leetcode-cn.com/problems/the-skyline-problem/solution/tian-ji-xian-wen-ti-shun-xu-sao-miao-ji-zj0ox/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

