#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#eas
'''
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
1    
2 2
34 43
5678 8765   
首先我们对这棵树根节点的左子树进行前序遍历: pre_order = [2,3,5,6,4,7,8]

接着我们对这棵树根节点的右子树进行后序遍历：post_order = [8,7,4,6,5,3,2]

根据两次遍历我们不难发现 post_order 就是 pre_order的逆序，其实这也是对称二叉树的一个性质，根据这一点就不难写出代码了。

'''
#@lc code=start
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        bli = []     # 用来存左子树的前序遍历
        fli = []     # 用来存右子树的后序遍历
        if root == None:   # 无根节点
            return True
        if root and root.left == None and root.right == None:  # 只有根节点
            return True
        if root.left == None or root.right == None:
            return False

        if root and root.left and root.right:
            self.pre_order(root.left, bli)
            self.post_order(root.right, fli)
            fli.reverse()            # 将后序遍历的列表倒序
            if bli == fli:
                return True
            else:
                return False

    def pre_order(self,root,li):    # 二叉树的前序遍历
        if root:
            li.append(root.val)
            self.pre_order(root.left,li)
            self.pre_order(root.right,li)
        elif root == None:
            li.append(None)

    def post_order(self,root,li):   # 二叉树的后序遍历
        if root:
            self.post_order(root.left,li)
            self.post_order(root.right,li)
            li.append(root.val)
        elif root == None:
            li.append(None)
    '''

作者：han-han-a-gou
链接：https://leetcode-cn.com/problems/symmetric-tree/solution/python3-yi-ge-hao-li-jie-de-shen-qi-jie-fa-by-han-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''

# @lc code=end

