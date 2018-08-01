# 二叉树的所有路径

# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
            递归即可.
        :type root: TreeNode
        :rtype: List[str]
        """
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self, node, path, result):
        # path: 存储当前遍历到的节点集合
        # result: 最终结果
        # node: 当前遍历到的节点

        # 如果当前节点为空.
        if node is None:
            return
        # 当前节点为根节点时, 将当前路径加入结果集
        if node.left is node.right is None:
            ans = ''.join([str(n.val) + '->' for n in path])
            result.append(ans + str(node.val))
            return

            # 遍历左节点
        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        # 遍历右节点
        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()
