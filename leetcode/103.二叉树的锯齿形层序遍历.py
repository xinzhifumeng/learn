#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#medium
'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]


作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvle7s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        row = 0
        dq = deque()
        dq.append(root)

        while dq:
            cur_size = len(dq)
            row += 1
            odd = row % 2
            temp = []
            for i in range(cur_size):
                if odd == 1:
                    cur = dq.popleft()
                    temp.append(cur.val)
                    if cur.left: dq.append(cur.left)
                    if cur.right: dq.append(cur.right)
                else:
                    cur = dq.pop()
                    temp.append(cur.val)
                    if cur.right: dq.appendleft(cur.right)
                    if cur.left: dq.appendleft(cur.left)
            res.append(temp)
        return res
'''
作者：mei-56
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/python-shuang-duan-dui-lie-bfs-by-mei-56-5c18/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

