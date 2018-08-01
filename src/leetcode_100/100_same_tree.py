# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
# 输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
            递归比较即可..
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False