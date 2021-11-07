#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#easy
'''
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

 

示例 1：


输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
示例 2：


输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
示例 3：

输入: root = [2,1,3], k = 4
输出: true
示例 4：

输入: root = [2,1,3], k = 1
输出: false
示例 5：

输入: root = [2,1,3], k = 3
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
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
    def findTarget(self, root: TreeNode, k: int) -> bool:

        #dfs + 字典
        us = set()

        def dfs_NLR(x: TreeNode) -> bool:
            nonlocal us
            if x == None:
                return False
            if k - x.val in us:
                return True
            us.add(x.val)
            return dfs_NLR(x.left) or dfs_NLR(x.right)
        
        return dfs_NLR(root)
        '''
        bfs + 字典

        us = set()
        q = collections.deque()
        q.append(root)
        while q:
            x = q.pop()

            if k - x.val in us:
                return True
            us.add(x.val)

            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
                
        return False

作者：Hanxin_Hanxin
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/solution/cpython3java-1dfswu-xu-zi-dian-2bfswu-xu-51m4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''


# @lc code=end

