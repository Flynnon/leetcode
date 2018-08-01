# 二叉树的锯齿形层次遍历
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
            与 102 类似, 只需要加一个反转标记即可
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        cur_line, result = [root], []
        right_flag = True
        while cur_line:
            next_line, tmps = [], []
            for node in cur_line:
                tmps.append(node.val)
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
            result.append(tmps if right_flag else tmps[::-1])
            right_flag = not right_flag
            cur_line = next_line
        return result