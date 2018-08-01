# 平衡二叉树

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
            递归判断每一个节点是否满足条件即可. 遇到不满足条件的节点，结果向上传导.
        :type root: TreeNode
        :rtype: bool
        """

        return self.getHeight(root) >= 0

    def getHeight(self, root):
        if root is None:
            return 0
        # 左子树高度, 右子树高度
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
        # 如果 左子树 或 右子树 或 当前节点 不满足条件, 返回 -1  也就是说,一旦某个节点不满足条件,它之上的所有节点均不满足条件
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        # 返回当前最大深度
        return max(left_height, right_height) + 1
