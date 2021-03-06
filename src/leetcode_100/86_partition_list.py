# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
            拆成两个链表
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_smaller, dummy_greater = ListNode(-1), ListNode(-1)
        smaller, greater = dummy_smaller, dummy_greater

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        smaller.next = dummy_greater.next
        greater.next = None

        return dummy_smaller.next