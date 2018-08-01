# 有序数组转换二叉搜索树
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.child_tree(nums, 0, len(nums) - 1)

    def child_tree(self, array, left_index, right_index):
        if left_index > right_index:
            return None
        mid = (left_index + right_index) // 2
        cur_node = TreeNode(array[mid])
        cur_node.left = self.child_tree(array, left_index, mid - 1)
        cur_node.right = self.child_tree(array, mid + 1, right_index)
        return cur_node
