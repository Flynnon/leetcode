# 二叉搜索树迭代器

#  实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
#
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
#
# 注意: next() 和hasNext() 操作的时间复杂度是O(1)，并使用 O(h) 内存，其中 h 是树的高度。


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    """
       二叉搜索树：空树或者二叉树的所有节点比他的左子节点大，比他的右子节点小.
       因此这实际上就是一个中序遍历的过程.
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # 使用栈保存中序遍历的路径
        self.stack = []
        self.cur = root

    def hasNext(self):
        """
        :rtype: bool
        """
        # 当还有元素没遍历时，就还有节点
        return self.stack or self.cur

    def next(self):
        """
        :rtype: int
        """
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        self.cur = self.stack.pop()
        node = self.cur
        self.cur = self.cur.right

        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())