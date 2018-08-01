# 填充同一层的兄弟节点

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
# 你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
# 示例:
#
# 给定完美二叉树，
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# 调用你的函数后，该完美二叉树变为：
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL


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
            遍历每个节点时,设置其子节点的兄弟节点即可. 注意 最后一列的节点本身没有兄弟节点,也无需设置..
        :param root: TreeLinkNode
        :return:
        """
        head = root
        while head:
            prev, cur, next_head = None, head, None
            # 如果当前不是最后一行(最后一行才没有左子节点) 且 当前行还没结束
            while cur and cur.left:
                # 设置左子节点的兄弟节点
                cur.left.next = cur.right
                # 如果当前节点不是最右列的节点
                if cur.next:
                    # 设置其右子节点的兄弟节点
                    cur.right.next = cur.next.left
                # 遍历下一个节点
                cur = cur.next
            # 向下移动一行
            head = head.left