#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
#树具有的特点有：

#（1）每个结点有零个或多个子结点

#（2）没有父节点的结点称为根节点

#（3）每一个非根结点有且只有一个父节点

#（4）除了根结点外，每个子结点可以分为多个不相交的子树。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
# @lc code=end

