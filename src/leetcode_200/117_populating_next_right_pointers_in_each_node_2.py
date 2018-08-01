# 填充同一层的兄弟节点 II

# 给定一个二叉树
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 说明:
#
# 你只能使用额外常数空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 示例:
#
# 给定二叉树，
#
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# 调用你的函数后，该二叉树变为：
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
            # TODO
            相比 116 少了 完美二叉树的约束

        :param root:
        """
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head = cur.left
                    elif cur.right:
                        next_head = cur.right

                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next
            head = next_head
