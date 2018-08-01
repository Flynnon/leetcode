# 删除链表中的节点

# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
            直接遍历删除即可
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre and pre.next:
            t = pre.next
            if t.val == val:
                pre.next = t.next
            else:
                pre = pre.next
        return dummy.next