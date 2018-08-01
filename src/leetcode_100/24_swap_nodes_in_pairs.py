# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 说明:
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
            直接转就好....注意别弄断...
        :type head: ListNode
        :rtype: ListNode
        """
        # 使用哑结点简化操作
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next