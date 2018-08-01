# 翻转二叉树

# 翻转一棵二叉树。
#
# 示例：
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#   谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
            递归反转即可
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


class Solution2:
    def invertTree(self, root):
        """
            与层序遍历类似，使用辅助队列即可(先右后左，子树反转)
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            node.left, node.right = node.right, node.left
        return root

