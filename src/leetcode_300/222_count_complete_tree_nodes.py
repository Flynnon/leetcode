# 完全二叉树的节点个数

# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
#     并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
            递归求解，分别判断左右子树是否为满二叉树，是满二叉树或者叶子节点则直接根据公式得到节点个数
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = right_depth = 0
        t_left = root
        t_right = root
        while t_left:
            left_depth += 1
            t_left = t_left.left
        while t_right:
            right_depth += 1
            t_right = t_right.right
        if left_depth == right_depth:
            return 2 ** left_depth - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
