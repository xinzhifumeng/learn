#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#medium
'''
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

 

示例 1：


输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
示例 2：


输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
''''
作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/subtree-of-another-tree/solution/dui-cheng-mei-pan-duan-zi-shu-vs-pan-duan-xiang-de/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# @lc code=end

