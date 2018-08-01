# 二叉树的后序遍历


# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def postorderTraversal(self, root):
        """
            递归处理
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        self.post_rsu(root, result)
        return result

    def post_rsu(self, root, result):
        if not root:
            return
        self.post_rsu(root.left, result)
        self.post_rsu(root.right, result)
        result.append(root.val)


class Solution2:
    def postorderTraversal(self, root):
        """
            使用栈保存遍历过的节点，当遍历到某个节点时，先判断有没有轮到它
            某节点的左右节点一定在它之前一个被访问
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        pre_node, result, stack = None, [], [root]
        while stack:
            # 当前轮到的节点
            cur_node = stack[-1]
            # 已经轮到当前节点了( 当前节点已经是叶子节点 或者 当前节点的子节点都被访问过了 )
            if (cur_node.left is None and cur_node.right is None) or (pre_node and (pre_node is cur_node.left or
                                                                                    pre_node is cur_node.right)):
                result.append(cur_node.val)
                pre_node = cur_node
                stack.pop()
            # 没有轮到当前节点，就把它的子节点入栈
            else:
                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)
        return result
