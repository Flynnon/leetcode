# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 示例
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isValidBST(self, root):
        """
            递归解. 中序遍历
            注意有 最大值 和 最小值
        :type root: TreeNode
        :rtype: bool
        """

        return self.valid_bst(root, float('-inf'), float('inf'))

    def valid_bst(self, node, min_value, max_value):
        if not node:
            return True

        return min_value < node.val < max_value and \
               self.valid_bst(node.left, min_value, node.val) and \
               self.valid_bst(node.right, node.val, max_value)
