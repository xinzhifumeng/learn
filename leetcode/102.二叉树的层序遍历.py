#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
'''
144前序遍历 递归解法
94 中序遍历 迭代解法
145后序遍历 
102层序遍历
前三个对应头结点位置不同

'''
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        res, q = [], [root]
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.pop(0)
                #这里的q相当于一个队列
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res



# @lc code=end

