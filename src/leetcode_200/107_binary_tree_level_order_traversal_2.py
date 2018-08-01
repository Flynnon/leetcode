# 二叉树的层序遍历II
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
            与 102 类似
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result, cur_line = [], [root]

        while cur_line:
            next_line, tmp_vals = [], []
            for node in cur_line:
                tmp_vals.append(node.val)
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
            cur_line = next_line
            result.insert(0, tmp_vals)

        return result

