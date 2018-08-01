# 二叉树的前序遍历


# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def preorderTraversal(self, root):
        """
            使用栈存放下一步要遍历的节点
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


class Solution2(object):
    def preorderTraversal(self, root):
        """
            递归处理
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.pre_rsu(root, result)
        return result

    def pre_rsu(self, root, result, ):
        if not root:
            return
        result.append(root.val)
        self.pre_rsu(root.left, result)
        self.pre_rsu(root.right, result)

