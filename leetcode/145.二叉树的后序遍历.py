#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            nonlocal res #可使用上一级定义的res
            if not root: return 

            dfs(root.left) #left
            dfs(root.right) #right
            res.append(root.val) #将根结点加入结果
            
            #前中后的遍历只需要改变def中的顺序即可
        dfs(root)
        return res

# @lc code=end

