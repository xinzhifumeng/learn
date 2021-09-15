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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        #递归方法
        if not root:
            return []

        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res
        '''
        
        
        # 迭代
        res, stack = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
'''
#morris方法（将二叉树转化为链表，每一个node都只可能有右孩子
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if root.left:
                # find out predecessor
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                # link predecessor to root
                predecessor.right = root
                # set left child of root to None
                temp = root
                root = root.left
                temp.left = None
            else:
                res.append(root.val)
                root = root.right
        return res
'''

        
        


# @lc code=end

