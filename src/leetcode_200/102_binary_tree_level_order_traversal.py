# 二叉树的层序遍历

# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
            使用两个队列进行存储....
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        cur_line = [root]
        result = []
        while cur_line:
            next_line, tmps = [], []
            for node in cur_line:
                tmps.append(node.val)
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
            result.append(tmps)
            cur_line = next_line
        return result