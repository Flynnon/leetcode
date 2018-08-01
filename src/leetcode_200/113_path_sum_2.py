# 路径之和 2


# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, _sum):
        """
            深度优先遍历  DFS.遇到满足条件的就放到结果集中.
        :type root: TreeNode
        :type _sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.pathSumRecu(result, [], root, _sum)
        return result

    def pathSumRecu(self, result, cur, root, _sum):

        # 节点不存在
        if root is None:
            return

        # 能匹配上时, 将当前路径加入结果集, 并返回
        if root.left is None and root.right is None and root.val == _sum:
            result.append(cur + [root.val])
            return

        # 使用cur保存当前遍历过的元素
        cur.append(root.val)
        self.pathSumRecu(result, cur, root.left, _sum - root.val)
        self.pathSumRecu(result, cur, root.right, _sum - root.val)
        # 恢复原样
        cur.pop()
        return
