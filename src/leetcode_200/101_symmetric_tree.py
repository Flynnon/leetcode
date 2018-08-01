# 对称二叉树

# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isSymmetric(self, root):
        """
            递归解法
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        # left - right 一对儿对称的节点

        # 对称节点均为None时, True
        if left is None and right is None:
            return True
        # 当前对称节点不对称, False
        if left is None or right is None or left.val != right.val:
            return False
        # 左节点的左节点 与 右节点的右节点 是否对称. 左节点的右节点 与 右节点的左节点 是否对称.
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)


class Solution2:
    def isSymmetric(self, root):
        """
            非递归解法
            使用栈模拟递归
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = [root.left, root.right]

        while stack:
            left_node, right_node = stack.pop(), stack.pop()

            if left_node is None and right_node is None:
                continue

            if left_node is None or right_node is None or left_node.val != right_node.val:
                return False

            stack.append(left_node.left)
            stack.append(right_node.right)

            stack.append(left_node.right)
            stack.append(right_node.left)

        return True