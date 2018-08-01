# 二叉树展开为链表

# 给定一个二叉树，原地将它展开为链表。(前序遍历???)
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
            前序遍历, 碰到新节点时, 将它的左节点变成右节点..
            节点全部使用 栈 保存, 因此无需担心断掉
            http://yuanhsh.iteye.com/blog/2185978
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = [root]
        leaf = root
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            if leaf is not node:
                leaf.left = None
                leaf.right = node
                leaf = node
