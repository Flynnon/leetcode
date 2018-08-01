# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def inorderTraversal(self, root):
        """
            递归解法
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.do_traversal(result, root)
        return result

    def do_traversal(self, result, node):
        """
        :type node: TreeNode
        :type result: list
        """
        if not node:
            return
        if node.left:
            self.do_traversal(result, node.left)
        result.append(node.val)
        if node.right:
            self.do_traversal(result, node.right)


class Solution2:
    def inorderTraversal(self, root):
        """
            迭代解法
            模拟递归的过程，将左子树节点不断的压入栈，直到左叶子，然后处理栈顶节点的右子树
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result
